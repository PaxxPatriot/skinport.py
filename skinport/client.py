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

from typing import List, Union


from .enums import AppID, Currency
from .errors import ParamRequired
from .http import HTTPClient
from .item import Item, ItemWithSales, ItemOutOfStock
from .iterators import TransactionAsyncIterator
from .transaction import Credit, Withdraw, Purchase


__all__ = ("Client",)


class Client:
    def __init__(self):
        self.http: HTTPClient = HTTPClient()
        self._closed = False

    def set_auth(self, *, client_id: str, client_secret: str):
        self.http.set_auth(client_id, client_secret)

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
        currency: Currency = Currency.eur,
        tradable: bool = False,
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
        params = {
            "app_id": app_id,
            "currency": currency.value,
            "tradable": _tradable,
        }
        data = await self.http.get_items(params=params)
        return [Item(data=item) for item in data]

    async def get_sales_history(
        self,
        *market_hash_names: str,
        app_id: int = 730,
        currency: Currency = Currency.eur,
    ) -> List[ItemWithSales]:  # sourcery skip: default-mutable-arg
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
        if not market_hash_names:
            raise ParamRequired("At least one market_hash_name is required.")
        params = {
            "market_hash_name": ",".join(market_hash_names),
            "app_id": app_id,
            "currency": currency.value,
        }
        data = await self.http.get_sales_history(params=params)
        return [ItemWithSales(data=sale) for sale in data]

    async def get_sales_out_of_stock(
        self, *, app_id: int = 730, currency: Currency = Currency.eur
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
        params = {"app_id": app_id, "currency": currency.value}
        data = await self.http.get_sales_out_of_stock(params=params)
        return [ItemOutOfStock(data=sale) for sale in data]

    async def get_account_transactions(
        self, *, page: int = 1, limit: int = 100, order: str = "desc"
    ) -> List[Union[Credit, Withdraw, Purchase]]:
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
        :class:`TransactionAsyncIterator` of :class:`.Item`

        Raises
        ------
        :exc:`AuthenticationError`
        """
        return TransactionAsyncIterator(self.http.get_account_transactions)
