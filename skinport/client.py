"""
MIT License

Copyright (c) 2022 PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
import logging
import signal
from typing import Any, Coroutine, Dict, List, Union

import socketio
from asyncache import cached
from cachetools import TTLCache

from .enums import AppID, Currency, Locale
from .errors import ParamRequired
from .http import HTTPClient
from .item import Item, ItemOutOfStock, ItemWithSales
from .iterators import TransactionAsyncIterator
from .transaction import Credit, Purchase, Withdraw

__all__ = ("Client",)


_log = logging.getLogger(__name__)


def _cancel_tasks(loop: asyncio.AbstractEventLoop) -> None:
    tasks = {t for t in asyncio.all_tasks(loop=loop) if not t.done()}

    if not tasks:
        return

    _log.info("Cleaning up after %d tasks.", len(tasks))
    for task in tasks:
        task.cancel()

    loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
    _log.info("All tasks finished cancelling.")

    for task in tasks:
        if task.cancelled():
            continue
        if task.exception() is not None:
            loop.call_exception_handler(
                {
                    "message": "Unhandled exception during Client.run shutdown.",
                    "exception": task.exception(),
                    "task": task,
                }
            )


def _cleanup_loop(loop: asyncio.AbstractEventLoop) -> None:
    try:
        _cancel_tasks(loop)
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        _log.info("Closing the event loop.")
        loop.close()


class Client:
    def __init__(self, debug: bool = False):
        self.http: HTTPClient = HTTPClient()
        self.ws: socketio.AsyncClient = socketio.AsyncClient(logger=debug, engineio_logger=debug)
        self._connected = False

    def set_auth(self, *, client_id: str, client_secret: str):
        self.http.set_auth(client_id, client_secret)

    def run(
        self,
        *,
        app_id: AppID = AppID.csgo,
        currency: Currency = Currency.eur,
        locale: Locale = Locale.en,
    ) -> None:
        """A blocking call that abstracts away the event loop
        initialisation from you.
        If you want more control over the event loop then this
        function should not be used. Use :meth:`connect`.

        Parameters
        ----------
        app_id: :class:`AppID`
            The app_id for the inventory's game.
            Defaults to ``AppID.csgo``.
        currency: :class:`Currency`
            The currency for pricing.
            Defaults to ``Currency.eur``.
        locale: :class:`Locale`
            Whether or not to show only tradable items.
            Defaults to ``Locale.en``.

        .. warning::

            This function must be the last function to call due to the fact that it
            is blocking. That means that registration of events or anything being
            called after this function call will not execute until it returns.
        """
        loop = asyncio.get_event_loop()

        try:
            loop.add_signal_handler(signal.SIGINT, lambda: loop.stop())
            loop.add_signal_handler(signal.SIGTERM, lambda: loop.stop())
        except NotImplementedError:
            pass

        async def runner():
            try:
                await self.connect(app_id=app_id, currency=currency, locale=locale)
            finally:
                if self._connected:
                    await self.close()

        def stop_loop_on_completion(f):
            loop.stop()

        future = asyncio.ensure_future(runner(), loop=loop)
        future.add_done_callback(stop_loop_on_completion)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            _log.info("Received signal to terminate bot and event loop.")
        finally:
            future.remove_done_callback(stop_loop_on_completion)
            _log.info("Cleaning up tasks.")
            _cleanup_loop(loop)

        if not future.cancelled():
            try:
                return future.result()
            except KeyboardInterrupt:
                # I am unsure why this gets raised here but suppress it anyway
                return None

    async def catch_all(self, event, data):
        _log.debug(f"Received event {event}")

    def listen(self, name: str = None) -> Coroutine[Any, Any, Any]:
        """A decorator that registers an event listener.
        The events must be a coroutine, if not, :exc:`TypeError` is raised.
        Example
        ---------
        .. code-block:: python3

           @client.listen("saleFeed")
           async def on_sale_feed(data):
               print(data)

        Raises
        --------
        TypeError
            The coroutine passed is not actually a coroutine.
        """

        def decorator(func):
            if not asyncio.iscoroutinefunction(func):
                raise TypeError("event listener registered must be a coroutine function")

            if name is None:
                raise ValueError("name can't be None")

            self.ws.on(name, func)
            _log.debug("%s has successfully been registered as an event", func.__name__)
            return func

        return decorator

    async def connect(
        self,
        *,
        app_id: AppID = AppID.csgo,
        currency: Currency = Currency.eur,
        locale: Locale = Locale.en,
    ) -> None:
        """*coroutine*
        Connects to the socket.io websocket.

        Parameters
        ----------
        app_id: :class:`AppID`
            The app_id for the inventory's game.
            Defaults to ``730``.
        currency: :class:`Currency`
            The currency for pricing.
            Defaults to ``EUR``.
        locale: :class:`Locale`
            Whether or not to show only tradable items.
            Defaults to ``en``.
        """
        kwargs = {"app_id": app_id, "currency": currency, "locale": locale}
        # Get parameters for the sale feed
        if self._connected:
            _log.info("Client is already connected. Closing the existing connection.")
            await self.close()

        try:
            self.ws.on("*", self.catch_all)
            self.ws.on("connect", lambda: asyncio.ensure_future(self.on_connect(**kwargs)))
            await self.ws.connect("https://skinport.com", transports=["websocket"], retry=True)
            self._connected = True
            await self.ws.wait()
        except asyncio.TimeoutError:
            _log.info("Connection timed out.")
            await self.close()
            self._connected = False
        except socketio.exceptions.ConnectionError:
            _log.warning("Client is already connected. Skipping connection attempt.")

    async def on_connect(self, **kwargs: Any) -> None:
        _log.info("Connected to Skinport. Emitting saleFeedJoin event...")
        await self._emit_sale_feed_join(kwargs)

    async def _emit_sale_feed_join(self, kwargs: Dict[str, Any]) -> None:
        app_id = kwargs.get("app_id", AppID.csgo)
        currency = kwargs.get("currency", Currency.eur)
        locale = kwargs.get("locale", Locale.en)
        await self.ws.emit(
            "saleFeedJoin",
            {
                "currency": currency.value,
                "locale": locale.value,
                "appid": app_id.value,
            },
        )
        await self.ws.wait()

    async def close(self) -> None:
        """*coroutine*
        Closes the `aiohttp.ClientSession`.
        """
        # Always close the underlying session of the HTTPClient
        await self.http.close()

        if not self._connected:
            return

        self._connected = False
        if self.ws.eio.http is not None:
            await self.ws.eio.http.close()

    @cached(cache=TTLCache(maxsize=128, ttl=300))
    async def get_items(
        self,
        *,
        app_id: AppID = AppID.csgo,
        currency: Currency = Currency.eur,
        tradable: bool = False,
    ) -> List[Item]:
        """*coroutine*
        Returns a :class:`list` of :class:`Item`.

        Parameters
        ----------
        app_id: :class:`.AppID`
            The app_id for the inventory's game.
            Defaults to ``730``.
        currency: :class:`.Currency`
            The currency for pricing.
            Defaults to ``EUR``.
        tradable: :class:`bool`
            Whether or not to show only tradable items.
            Defaults to ``False``.

        Returns
        -------
        :class:`list` of :class:`Item`
        """

        _tradable = str(tradable).lower()
        params = {
            "app_id": app_id,
            "currency": currency.value,
            "tradable": _tradable,
        }
        data = await self.http.get_items(params=params)
        return [Item(data=item) for item in data]

    @cached(cache=TTLCache(maxsize=16, ttl=3600))
    async def get_sales_history(
        self,
        app_id: AppID = AppID.csgo,
        currency: Currency = Currency.eur,
    ) -> List[ItemWithSales]:  # sourcery skip: default-mutable-arg
        """*coroutine*
        Returns a :class:`list` of :class:`ItemWithSales`.

        Parameters
        ----------
        app_id: :class:`.AppID`
            The app_id for the inventory's game.
            Defaults to ``730``.
        currency: :class:`.Currency`
            The currency for pricing.
            Defaults to ``EUR``.

        Returns
        -------
        :class:`list` of :class:`ItemWithSales`
        """
        params = {
            "app_id": app_id,
            "currency": currency.value,
        }
        data = await self.http.get_sales_history(params=params)
        return [ItemWithSales(data=sale) for sale in data]

    @cached(cache=TTLCache(maxsize=16, ttl=3600))
    async def get_sales_out_of_stock(
        self, *, app_id: AppID = AppID.csgo, currency: Currency = Currency.eur
    ) -> List[ItemOutOfStock]:
        """*coroutine*
        Returns a :class:`list` of :class:`ItemOutOfStock`.

        Parameters
        ----------
        app_id: :class:`.AppID`
            The app_id for the inventory's game.
            Defaults to ``730``.
        currency: :class:`.Currency`
            The currency for pricing.
            Defaults to ``EUR``.

        Returns
        -------
        :class:`list` of :class:`ItemOutOfStock`
        """
        params = {"app_id": app_id, "currency": currency.value}
        data = await self.http.get_sales_out_of_stock(params=params)
        return [ItemOutOfStock(data=sale) for sale in data]

    async def get_account_transactions(
        self, *, page: int = 1, limit: int = 100, order: str = "desc"
    ) -> List[Union[Credit, Withdraw, Purchase]]:
        """*coroutine*
        Returns a :class:`list` of :class:`Transaction`.

        Parameters
        ----------
        page: :class:`int`
            Pagination Page.
            Defaults to ``1``.
        limit: :class:`int`
            Limit results between ``1`` and ``100``.
            Defaults to ``100``.
        order: :class:`str`
            Order results by asc or desc.
            Defaults to ``desc``.

        Returns
        -------
        :class:`list` of :class:`Transaction`

        Raises
        ------
        :exc:`AuthenticationError`
        """
        params = {"page": page, "limit": limit, "order": order}
        data = await self.http.get_account_transactions(params=params)

        transactions: List[Union[Credit, Withdraw, Purchase]] = []
        for transaction in data["data"]:
            if transaction["type"] == "credit":
                transactions.append(Credit(data=transaction))
            elif transaction["type"] == "withdraw":
                transactions.append(Withdraw(data=transaction))
            elif transaction["type"] == "purchase":
                transactions.append(Purchase(data=transaction))

        return transactions

    async def fetch_all_account_transactions(self) -> TransactionAsyncIterator:
        """
        Returns an AsyncIterator that iterates over all transactions of the authenticated client.


        Returns
        -------
        :class:`TransactionAsyncIterator` of :class:`Item`

        Raises
        ------
        :exc:`AuthenticationError`
        """
        return TransactionAsyncIterator(self.http.get_account_transactions)
