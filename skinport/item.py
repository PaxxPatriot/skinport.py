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
from typing import Any, Dict, List, Optional

from .enums import Currency
from .sale import LastXDays, Sale

__all__ = (
    "Item",
    "ItemWithSales",
    "ItemOutOfStock",
)


class Item:
    """Represents an item."""

    __slots__ = (
        "_market_hash_name",
        "_currency",
        "_suggested_price",
        "_item_page",
        "_market_page",
        "_min_price",
        "_max_price",
        "_mean_price",
        "_quantity",
        "_created_at",
        "_updated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._market_hash_name = data.get("market_hash_name", "")
        self._currency = data.get("currency")
        self._suggested_price = data.get("suggested_price")
        self._item_page = data.get("item_page", "")
        self._market_page = data.get("market_page", "")
        self._min_price = data.get("min_price")
        self._max_price = data.get("max_price")
        self._mean_price = data.get("mean_price")
        self._quantity = data.get("quantity", 0)
        self._created_at = data.get("created_at", 0)
        self._updated_at = data.get("updated_at", 0)

    def __repr__(self) -> str:
        return f"<Item market_hash_name={self._market_hash_name} market_page={self._market_page} quantity={self._quantity}>"

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
        "_market_hash_name",
        "_version",
        "_currency",
        "_suggested_price",
        "_avg_sale_price",
        "_sales_last_90d",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._market_hash_name = data.get("market_hash_name", "")
        self._version = data.get("version")
        self._currency = data.get("currency")
        self._suggested_price = data.get("suggested_price", 0.0)
        self._avg_sale_price = data.get("avg_sale_price", 0.0)
        self._sales_last_90d = data.get("sales_last_90d", 0)

    def __repr__(self) -> str:
        return f"SaleOutOfStock({{'market_hash_name': {self._market_hash_name}, 'version': {self._version}, 'currency': {self._currency}, 'suggested_price': {self._suggested_price}, 'avg_sale_price': {self._avg_sale_price}, 'sales_last_90d': {self._sales_last_90d}}}"

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
        "_market_hash_name",
        "_currency",
        "_item_page",
        "_market_page",
        "_sales",
        "_last_7_days",
        "_last_30_days",
        "_last_90_days",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._market_hash_name = data.get("market_hash_name", "")
        self._currency = data.get("currency")
        self._item_page = data.get("item_page", "")
        self._market_page = data.get("market_page", "")
        self._sales = data.get("sales", [])
        self._last_7_days = data.get("last_7_days", {})
        self._last_30_days = data.get("last_30_days", {})
        self._last_90_days = data.get("last_90_days", {})

    def __repr__(self) -> str:
        return f"<ItemWithSales market_hash_name={self._market_hash_name} Sales={len(self._sales)}>"

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str`: Returns the name of the item under it displayed on skinport.com."""
        return self._market_hash_name

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
    def sales(self) -> List[Sale]:
        """List[:class:`Sale`]: Returns a :class:`list` of :class:`Sale`."""
        return [Sale(data=sale) for sale in self._sales]

    @property
    def last_7_days(self) -> LastXDays:
        """:class:`LastXDays`: Returns the last 7 days of the item."""
        return LastXDays(data=self._last_7_days)

    @property
    def last_30_days(self) -> LastXDays:
        """:class:`LastXDays`: Returns the last 30 days of the item."""
        return LastXDays(data=self._last_30_days)

    @property
    def last_90_days(self) -> LastXDays:
        """:class:`LastXDays`: Returns the last 90 days of the item."""
        return LastXDays(data=self._last_90_days)
