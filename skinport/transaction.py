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

import datetime
from typing import List

from .enums import Currency

__all__ = ("Transaction", "TransactionItem")


class TransactionItem:
    """Represents an item from a transaction."""

    __slots__ = (
        "_sale_id",
        "_market_hash_name",
        "_seller_country",
        "_buyer_country",
    )

    def __init__(self, *, data) -> None:
        self._sale_id = data.get("sale_id")
        self._market_hash_name = data.get("market_hash_name")
        self._seller_country = data.get("seller_country")
        self._buyer_country = data.get("buyer_country")

    def __repr__(self) -> str:
        return f"TransactionItem({{'sale_id': {self._sale_id}, 'market_hash_name': {self._market_hash_name}, 'seller_country': {self._seller_country}, 'buyer_country': {self._buyer_country}}})"

    def __str__(self) -> str:
        return self._market_hash_name

    @property
    def sale_id(self) -> str:
        """Returns the sale ID."""
        return self._sale_id

    @property
    def market_hash_name(self) -> str:
        """Returns the market hash name."""
        return self._market_hash_name

    @property
    def seller_country(self) -> str:
        """Returns the seller country."""
        return self._seller_country

    @property
    def buyer_country(self) -> str:
        """Returns the buyer country."""
        return self._buyer_country


class Transaction:
    """Represents a transaction."""

    __slots__ = (
        "_transaction_id",
        "_type",
        "_sub_type",
        "_status",
        "_amount",
        "_fee",
        "_currency",
        "_items",
        "_created_at",
        "_updated_at",
    )

    def __init__(self, *, data) -> None:
        self._transaction_id = data.get("id")
        self._type = data.get("type")
        self._sub_type = data.get("sub_type")
        self._status = data.get("status")
        self._amount = data.get("amount")
        self._fee = data.get("fee")
        self._currency = data.get("currency")
        self._items = []
        if data.get("items") is not None:
            self._items = [TransactionItem(data=item) for item in data.get("items")]
        self._created_at = datetime.datetime.strptime(
            data.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self._updated_at = datetime.datetime.strptime(
            data.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%fZ"
        )

    def __repr__(self) -> str:
        return f"<Transaction {self._transaction_id}>"

    def __str__(self) -> str:
        return str(self._transaction_id)

    @property
    def transaction_id(self) -> str:
        """Returns the sale ID."""
        return self._transaction_id

    @property
    def type(self) -> str:
        """Returns the transaction type."""
        return self._type

    @property
    def sub_type(self) -> str:
        """Returns the transaction sub type."""
        return self._sub_type

    @property
    def status(self) -> str:
        """Returns the transaction status."""
        return self._status

    @property
    def amount(self) -> str:
        """Returns the transaction amount."""
        return self._amount

    @property
    def fee(self) -> str:
        """Returns the transaction fee."""
        return self._fee

    @property
    def currency(self) -> Currency:
        """Returns the transaction currency."""
        return self._currency

    @property
    def items(self) -> List[TransactionItem]:
        """Returns the transaction items."""
        return self._items

    @property
    def created_at(self) -> datetime.datetime:
        """Returns the date and time the transaction was created."""
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        """Returns the date and time the transaction was updated."""
        return self._updated_at
