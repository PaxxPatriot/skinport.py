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
from typing import Any, Dict, List

from .enums import Currency

__all__ = ("Transaction", "TransactionItem", "Credit", "Purchase", "Withdraw")


class TransactionItem:
    """Represents an item from a transaction."""

    __slots__ = (
        "_sale_id",
        "_market_hash_name",
        "_seller_country",
        "_buyer_country",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._sale_id: int = data.get("sale_id", 0)
        self._market_hash_name: str = data.get("market_hash_name", "")
        self._seller_country: str = data.get("seller_country", "")
        self._buyer_country: str = data.get("buyer_country", "")

    def __repr__(self) -> str:
        return f"TransactionItem({{'sale_id': {self._sale_id}, 'market_hash_name': {self._market_hash_name}, 'seller_country': {self._seller_country}, 'buyer_country': {self._buyer_country}}})"

    def __str__(self) -> str:
        return self._market_hash_name

    @property
    def sale_id(self) -> int:
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
        "_status",
        "_amount",
        "_currency",
        "_created_at",
        "_updated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._transaction_id: int = data.get("id", 0)
        self._type: str = data.get("type", "")
        self._status: str = data.get("status", "")
        self._amount: int = data.get("amount", 0)
        self._currency: str = data.get("currency", Currency.eur.value)
        self._created_at: str = data.get("created_at", "1970-01-01T00:00:00.000Z")
        self._updated_at: str = data.get("updated_at", "1970-01-01T00:00:00.000Z")

    @property
    def transaction_id(self) -> int:
        """Returns the sale ID."""
        return self._transaction_id

    @property
    def type(self) -> str:
        """Returns the transaction type."""
        return self._type

    @property
    def status(self) -> str:
        """Returns the transaction status."""
        return self._status

    @property
    def amount(self) -> int:
        """Returns the transaction amount."""
        return self._amount

    @property
    def currency(self) -> Currency:
        """Returns the transaction currency."""
        return Currency(self._currency)

    @property
    def created_at(self) -> datetime.datetime:
        """Returns the date and time the transaction was created."""
        return datetime.datetime.strptime(self._created_at, "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def updated_at(self) -> datetime.datetime:
        """Returns the date and time the transaction was updated."""
        return datetime.datetime.strptime(self._updated_at, "%Y-%m-%dT%H:%M:%S.%fZ")


class Credit(Transaction):
    """Represents a credit transaction."""

    __slots__ = (
        "_sub_type",
        "_fee",
        "_items",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        super().__init__(data=data)
        self._sub_type = data.get("sub_type", "")
        self._fee = data.get("fee", 0.0)
        self._items = [TransactionItem(data=item) for item in data.get("items", [])]

    def __repr__(self) -> str:
        return f"Credit({{'transaction_id': {self._transaction_id}, 'type': {self._type}, 'status': {self._status}, 'amount': {self._amount}, 'currency': {self._currency}, 'created_at': {self._created_at}, 'updated_at': {self._updated_at}, 'sub_type': {self._sub_type}, 'fee': {self._fee}, 'items': {self._items}}}"

    @property
    def sub_type(self) -> str:
        """Returns the transaction sub type."""
        return self._sub_type

    @property
    def fee(self) -> float:
        """Returns the transaction fee."""
        return self._fee

    @property
    def items(self) -> List[TransactionItem]:
        """Returns the transaction items."""
        return self._items


class Purchase(Transaction):
    """Represents a purchase transaction."""

    __slots__ = ("_items",)

    def __init__(self, *, data: Dict[str, Any]) -> None:
        super().__init__(data=data)
        self._items = [TransactionItem(data=item) for item in data.get("items", [])]

    def __repr__(self) -> str:
        return f"Purchase({{'transaction_id': {self._transaction_id}, 'type': {self._type}, 'status': {self._status}, 'amount': {self._amount}, 'currency': {self._currency}, 'created_at': {self._created_at}, 'updated_at': {self._updated_at}, 'items': {self._items}}}"

    @property
    def items(self) -> List[TransactionItem]:
        """Returns the transaction items."""
        return self._items


class Withdraw(Transaction):
    """Represents a withdraw transaction."""

    def __init__(self, *, data: Dict[str, Any]) -> None:
        super().__init__(data=data)

    def __repr__(self) -> str:
        return f"Withdraw({{'transaction_id': {self._transaction_id}, 'type': {self._type}, 'status': {self._status}, 'amount': {self._amount}, 'currency': {self._currency}, 'created_at': {self._created_at}, 'updated_at': {self._updated_at}}}"
