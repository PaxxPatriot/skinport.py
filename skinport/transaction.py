"""
MIT License

Copyright (c) 2022-present PaxxPatriot

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
from typing import Any, Dict, List, Optional

from .enums import Currency, TransactionType

__all__ = (
    "Transaction",
    "TransactionItem",
)


class TransactionItem:
    """Represents an item from a transaction."""

    __slots__ = (
        "_amount",
        "_asset_id",
        "_buyer_country",
        "_currency",
        "_market_hash_name",
        "_sale_id",
        "_seller_country",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._asset_id: int = data.get("asset_id", 0)
        self._sale_id: int = data.get("sale_id", 0)
        self._market_hash_name: str = data.get("market_hash_name", "")
        self._seller_country: str = data.get("seller_country", "")
        self._buyer_country: str = data.get("buyer_country", "")
        self._amount: float = data.get("amount", 0.0)
        self._currency: str = data.get("currency", Currency.eur.value)

    def __repr__(self) -> str:
        return f"TransactionItem(data={{'asset_id': {self._asset_id!r}, 'sale_id': {self._sale_id!r}, 'market_hash_name': {self._market_hash_name!r}, 'seller_country': {self._seller_country!r}, 'buyer_country': {self._buyer_country!r}, 'amount': {self._amount!r}, 'currency': {self._currency!r}}})"

    def __str__(self) -> str:
        return self._market_hash_name

    @property
    def asset_id(self) -> int:
        """Returns the asset ID."""
        return self._asset_id

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

    @property
    def amount(self) -> float:
        """Returns the amount of transaction item."""
        return self._amount

    @property
    def currency(self) -> Currency:
        """Returns the transaction item currency."""
        return Currency(self._currency)


class Transaction:
    """Represents a transaction."""

    __slots__ = (
        "_amount",
        "_created_at",
        "_currency",
        "_fee",
        "_items",
        "_status",
        "_sub_type",
        "_transaction_id",
        "_type",
        "_updated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._transaction_id: int = data.get("id")
        self._type: str = data.get("type")
        self._sub_type: Optional[str] = data.get("sub_type")
        self._status: str = data.get("status")
        self._amount: float = data.get("amount")
        self._fee: Optional[float] = data.get("fee")
        self._currency: str = data.get("currency")
        self._items: Optional[List[TransactionItem]] = (
            [TransactionItem(data=item) for item in data.get("items")] if data.get("items") is not None else None
        )
        self._created_at: str = data.get("created_at")
        self._updated_at: str = data.get("updated_at")

    def __repr__(self) -> str:
        return f"Transaction(data={{'id': {self._transaction_id!r}, 'type': {self._type!r}, 'sub_type': {self._sub_type!r}, 'status': {self._status!r}, 'amount': {self._amount!r}, 'fee': {self._fee!r}, 'currency': {self._currency!r}, 'items': {self._items!r}, 'created_at': {self._created_at!r}, 'updated_at': {self._updated_at!r}}})"

    @property
    def transaction_id(self) -> int:
        """:class:`int`: Returns the sale ID."""
        return self._transaction_id

    @property
    def type(self) -> TransactionType:
        """:class:`str`: Returns the transaction type."""
        return TransactionType(self._type)

    @property
    def sub_type(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the transaction subtype."""
        return self._sub_type

    @property
    def status(self) -> str:
        """:class:`str`: Returns the transaction status."""
        return self._status

    @property
    def amount(self) -> float:
        """:class:`float`: Returns the transaction amount."""
        return self._amount

    @property
    def fee(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the fee for the transaction."""
        return self._fee

    @property
    def currency(self) -> Currency:
        """:class:`Currency`: Returns the transaction currency."""
        return Currency(self._currency)

    @property
    def items(self) -> Optional[List[TransactionItem]]:
        """Optional[List[:class:`float`]]: Returns the transaction items."""
        return self._items

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the date and time the transaction was created."""
        return datetime.datetime.strptime(self._created_at, "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def updated_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the date and time the transaction was updated."""
        return datetime.datetime.strptime(self._updated_at, "%Y-%m-%dT%H:%M:%S.%fZ")
