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
from typing import Any, Dict, Optional

from .enums import Currency
from .sale import LastXDays

__all__ = (
    "Item",
    "ItemOutOfStock",
    "ItemWithSales",
)


class Item:
    """Represents an item."""

    __slots__ = (
        "_created_at",
        "_currency",
        "_item_page",
        "_market_hash_name",
        "_market_page",
        "_max_price",
        "_mean_price",
        "_median_price",
        "_min_price",
        "_quantity",
        "_suggested_price",
        "_updated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._market_hash_name = data.get("market_hash_name")
        self._currency = data.get("currency")
        self._suggested_price = data.get("suggested_price")
        self._item_page = data.get("item_page")
        self._market_page = data.get("market_page")
        self._min_price = data.get("min_price")
        self._max_price = data.get("max_price")
        self._mean_price = data.get("mean_price")
        self._median_price = data.get("median_price")
        self._quantity = data.get("quantity")
        self._created_at = data.get("created_at")
        self._updated_at = data.get("updated_at")

    def __repr__(self) -> str:
        return f"Item(data={{'market_hash_name': {self._market_hash_name!r}, 'currency': {self._currency!r}, 'suggested_price': {self._suggested_price!r}, 'item_page': {self._item_page!r}, 'market_page': {self._market_page!r}, 'min_price': {self._min_price!r}, 'max_price': {self._max_price!r}, 'mean_price': {self._mean_price!r}, 'median_price': {self._median_price!r}, 'quantity': {self._quantity!r}, 'created_at': {self._created_at!r}, 'updated_at': {self._updated_at!r}}})"

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str`: Returns the name of the item under it is displayed on skinport.com."""
        return self._market_hash_name

    @property
    def currency(self) -> Currency:
        """:class:`Currency`: Returns the currency of the item."""
        return Currency(self._currency)

    @property
    def suggested_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the suggested price of the item."""
        return self._suggested_price

    @property
    def item_page(self) -> str:
        """:class:`str`: Returns the item page of the item."""
        return self._item_page

    @property
    def market_page(self) -> str:
        """:class:`str`: Returns the market page of the item."""
        return self._market_page

    @property
    def min_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the min price of the item."""
        return self._min_price

    @property
    def max_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the max price of the item."""
        return self._max_price

    @property
    def mean_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the mean price of the item."""
        return self._mean_price

    @property
    def median_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the median price of the item."""
        return self._median_price

    @property
    def quantity(self) -> int:
        """:class:`int`: Returns the quantity of the item."""
        return self._quantity

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the created at of the item."""
        return datetime.datetime.fromtimestamp(self._created_at)

    @property
    def updated_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the updated at of the item."""
        return datetime.datetime.fromtimestamp(self._updated_at)


class ItemOutOfStock:
    """Represents an item which is out of stock."""

    __slots__ = (
        "_avg_sale_price",
        "_currency",
        "_market_hash_name",
        "_sales_last_90d",
        "_suggested_price",
        "_version",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._market_hash_name = data.get("market_hash_name")
        self._version = data.get("version")
        self._currency = data.get("currency")
        self._suggested_price = data.get("suggested_price")
        self._avg_sale_price = data.get("avg_sale_price")
        self._sales_last_90d = data.get("sales_last_90d")

    def __repr__(self) -> str:
        return f"ItemOutOfStock(data={{'market_hash_name': {self._market_hash_name!r}, 'version': {self._version!r}, 'currency': {self._currency!r}, 'suggested_price': {self._suggested_price!r}, 'avg_sale_price': {self._avg_sale_price!r}, 'sales_last_90d': {self._sales_last_90d!r}}}"

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str` Returns the market hash name of the item."""
        return self._market_hash_name

    @property
    def version(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the version of the item."""
        return self._version

    @property
    def currency(self) -> Currency:
        """:class:`Currency`: Returns the currency of the item."""
        return Currency(self._currency)

    @property
    def suggested_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the suggested price of the item."""
        return self._suggested_price

    @property
    def avg_sale_price(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the avg sale price of the item."""
        return self._avg_sale_price

    @property
    def sales_last_90d(self) -> int:
        """:class:`int`: Returns the sales last 90d of the item."""
        return self._sales_last_90d


class ItemWithSales:
    """Represents an item with sales history."""

    __slots__ = (
        "_currency",
        "_item_page",
        "_last_7_days",
        "_last_24_hours",
        "_last_30_days",
        "_last_90_days",
        "_market_hash_name",
        "_market_page",
        "_version",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._market_hash_name = data.get("market_hash_name", "")
        self._version = data.get("version", None)
        self._currency = data.get("currency")
        self._item_page = data.get("item_page", "")
        self._market_page = data.get("market_page", "")
        self._last_24_hours = data.get("last_24_hours", {})
        self._last_7_days = data.get("last_7_days", {})
        self._last_30_days = data.get("last_30_days", {})
        self._last_90_days = data.get("last_90_days", {})

    def __repr__(self) -> str:
        return f"ItemWithSales(data={{'market_hash_name': {self._market_hash_name!r}, 'version': {self._version!r}, 'currency': {self._currency!r}, 'item_page': {self._item_page!r}, 'market_page': {self._market_page!r}, 'last_24_hours': {self._last_24_hours!r}, 'last_7_days': {self._last_7_days!r}, 'last_30_days': {self._last_30_days!r}, 'last_90_days': {self._last_90_days!r}}})"

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str`: Returns the name of the item under it displayed on skinport.com."""
        return self._market_hash_name

    @property
    def version(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the version of the item."""
        return self._version

    @property
    def currency(self) -> Currency:
        """:class:`Currency`: Returns the currency of the item."""
        return Currency(self._currency)

    @property
    def item_page(self) -> str:
        """:class:`str`: Returns the item page of the item."""
        return self._item_page

    @property
    def market_page(self) -> str:
        """:class:`str`: Returns the market page of the item."""
        return self._market_page

    @property
    def last_24_hours(self) -> LastXDays:
        """:class:`LastXDays`: Returns information about sales of the item in the last 24 hours."""
        return LastXDays(data=self._last_24_hours)

    @property
    def last_7_days(self) -> LastXDays:
        """:class:`LastXDays`: Returns information about sales of the item in the last 7 days."""
        return LastXDays(data=self._last_7_days)

    @property
    def last_30_days(self) -> LastXDays:
        """:class:`LastXDays`: Returns information about sales of the item in the last 30 days."""
        return LastXDays(data=self._last_30_days)

    @property
    def last_90_days(self) -> LastXDays:
        """:class:`LastXDays`: Returns information about sales of the item in the last 90 days."""
        return LastXDays(data=self._last_90_days)
