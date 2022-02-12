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

from typing import List

from .enums import AppID, Currency
from .errors import ParamRequired, AuthenticationError

from .http import HTTPClient
from .sale import Sale
from .transaction import Transaction

from .item import Item, ItemWithSales, ItemOutOfStock

from .iterators import TransactionAsyncIterator

__all__ = ("Client",)


class Client:
    def __init__(self):
        self.http: HTTPClient = HTTPClient()
        self._closed = False

    async def login(self, client_id: str = None, client_secret: str = None):
        await self.http.set_token(client_id, client_secret)

    async def close(self) -> None:
        """*coroutine*
        Closes the `aiohttp.ClientSession`.
        """
        if self._closed:
            return

        self._closed = True
        await self.http.close()

    async def get_items(
        self,
        *,
        app_id: AppID = AppID.csgo,
        currency: Currency = "EUR",
        tradable: bool = False
    ) -> List[Item]:
        """*coroutine*
        Returns a :class:`list` of :class:`.Item`.

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
        :class:`list` of :class:`.Item`
        """

        _tradable = str(tradable).lower()
        params = {"app_id": app_id, "currency": currency, "tradable": _tradable}
        data = await self.http.get_items(params=params)
        return [Item(data=item) for item in data]

    async def get_sales_history(
        self,
        market_hash_name: List[str] = None,
        *,
        app_id: int = 730,
        currency: Currency = "EUR"
    ) -> List[ItemWithSales]:
        """*coroutine*
        Returns a :class:`list` of :class:`.ItemWithSales`.

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
        :class:`list` of :class:`.ItemWithSales`
        """
        if market_hash_name is None:
            raise ParamRequired("market_hash_name is required")
        params = {
            "market_hash_name": market_hash_name,
            "app_id": app_id,
            "currency": currency,
        }
        data = await self.http.get_sales_history(params=params)
        return [ItemWithSales(data=sale) for sale in data]

    async def get_sales_out_of_stock(
        self, *, app_id: int = 730, currency: Currency = "EUR"
    ) -> List[ItemOutOfStock]:
        """*coroutine*
        Returns a :class:`list` of :class:`.ItemOutOfStock`.

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
        :class:`list` of :class:`.ItemOutOfStock`
        """
        params = {"app_id": app_id, "currency": currency}
        data = await self.http.get_sales_out_of_stock(params=params)
        return [ItemOutOfStock(data=sale) for sale in data]

    async def get_account_transactions(
        self, *, page: int = 1, limit: int = 100, order: str = "desc"
    ) -> List[Transaction]:
        """*coroutine*
        Returns a :class:`list` of :class:`.Transaction`.

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
        :class:`list` of :class:`.Transaction`

        Raises
        ------
        :exc:`.AuthenticationError`
        """
        params = {"page": page, "limit": limit, "order": order}
        data = await self.http.get_account_transactions(params=params)
        return (
            [Transaction(data=transaction) for transaction in data["data"]]
            if data
            else []
        )

    async def fetch_all_account_transactions(self) -> List[Transaction]:
        """
        Returns an AsyncIterator that iterates over all transactions of the authenticated client.


        Returns
        -------
        :class:`TransactionAsyncIterator` of :class:`.Item`

        Raises
        ------
        :exc:`.AuthenticationError`
        """
        return TransactionAsyncIterator(self.http.get_account_transactions)
