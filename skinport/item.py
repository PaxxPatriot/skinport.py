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
from typing import Optional, List
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

    def __init__(self, *, data) -> None:
        self._market_hash_name = data.get("market_hash_name")
        self._currency = Currency(data.get("currency"))
        self._suggested_price = data.get("suggested_price")
        self._item_page = data.get("item_page")
        self._market_page = data.get("market_page")
        self._min_price = data.get("min_price")
        self._max_price = data.get("max_price")
        self._mean_price = data.get("mean_price")
        self._quantity = data.get("quantity")
        self._created_at = datetime.datetime.fromtimestamp(data.get("created_at"))
        self._updated_at = datetime.datetime.fromtimestamp(data.get("updated_at"))

    def __repr__(self) -> str:
        return (
            f"<Item {self._market_hash_name} {self._currency} {self._suggested_price}>"
        )

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str` Returns the name of the item under it displayed on skinport.com"""
        return self._market_hash_name

    @property
    def currency(self) -> Currency:
        """:class:`str` Returns the currency of the item"""
        return self._currency

    @property
    def suggested_price(self) -> float:
        """:class:`str` Returns the suggested price of the item"""
        return self._suggested_price

    @property
    def item_page(self) -> str:
        """:class:`str` Returns the item page of the item"""
        return self._item_page

    @property
    def market_page(self) -> str:
        """:class:`str` Returns the market page of the item"""
        return self._market_page

    @property
    def min_price(self) -> Optional[float]:
        """:class:`str` Returns the min price of the item"""
        return self._min_price

    @property
    def max_price(self) -> Optional[float]:
        """:class:`str` Returns the max price of the item"""
        return self._max_price

    @property
    def mean_price(self) -> Optional[float]:
        """:class:`str` Returns the mean price of the item"""
        return self._mean_price

    @property
    def quantity(self) -> int:
        """:class:`str` Returns the quantity of the item"""
        return self._quantity

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`str` Returns the created at of the item"""
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        """:class:`str` Returns the updated at of the item"""
        return self._updated_at


class ItemOutOfStock:

    __slots__ = (
        "_market_hash_name",
        "_version",
        "_currency",
        "_suggested_price",
        "_avg_sale_price",
        "_sales_last_90d",
    )

    def __init__(self, *, data) -> None:
        self._market_hash_name = data.get("market_hash_name")
        self._version = data.get("version")
        self._currency = data.get("currency")
        self._suggested_price = data.get("suggested_price")
        self._avg_sale_price = data.get("avg_sale_price")
        self._sales_last_90d = data.get("sales_last_90d")

    def __repr__(self) -> str:
        return f"SaleOutOfStock({{'market_hash_name': {self._market_hash_name}, 'version': {self._version}, 'currency': {self._currency}, 'suggested_price': {self._suggested_price}, 'avg_sale_price': {self._avg_sale_price}, 'sales_last_90d': {self._sales_last_90d}}}"

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str` Returns the market hash name of the item"""
        return self._market_hash_name

    @property
    def version(self) -> str:
        """:class:`str` Returns the version of the item"""
        return self._version

    @property
    def currency(self) -> Currency:
        """:class:`str` Returns the currency of the item"""
        return self._currency

    @property
    def suggested_price(self) -> float:
        """:class:`str` Returns the suggested price of the item"""
        return self._suggested_price

    @property
    def avg_sale_price(self) -> float:
        """:class:`str` Returns the avg sale price of the item"""
        return self._avg_sale_price

    @property
    def sales_last_90d(self) -> float:
        """:class:`str` Returns the sales last 90d of the item"""
        return self._sales_last_90d


class ItemWithSales:
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

    def __init__(self, *, data) -> None:
        self._market_hash_name = data.get("market_hash_name")
        self._currency = data.get("currency")
        self._item_page = data.get("item_page")
        self._market_page = data.get("market_page")
        self._sales = [Sale(data=sale) for sale in data.get("sales")]
        self._last_7_days = LastXDays(data=data.get("last_7_days"))
        self._last_30_days = LastXDays(data=data.get("last_30_days"))
        self._last_90_days = LastXDays(data=data.get("last_90_days"))

    def __repr__(self) -> str:
        return f"<ItemWithSales {self._market_hash_name} Sales={len(self._sales)}>"

    def __str__(self) -> str:
        return f"{self._market_hash_name}"

    @property
    def market_hash_name(self) -> str:
        """:class:`str` Returns the name of the item under it displayed on skinport.com"""
        return self._market_hash_name

    @property
    def currency(self) -> Currency:
        """:class:`str` Returns the currency of the item"""
        return self._currency

    @property
    def item_page(self) -> str:
        """:class:`str` Returns the item page of the item"""
        return self._item_page

    @property
    def market_page(self) -> str:
        """:class:`str` Returns the market page of the item"""
        return self._market_page

    @property
    def sales(self) -> List[Sale]:
        """:class:`str` Returns the sales of the item"""
        return self._sales

    @property
    def last_7_days(self) -> LastXDays:
        """:class:`str` Returns the last 7 days of the item"""
        return self._last_7_days

    @property
    def last_30_days(self) -> LastXDays:
        """:class:`str` Returns the last 30 days of the item"""
        return self._last_30_days

    @property
    def last_90_days(self) -> LastXDays:
        """:class:`str` Returns the last 90 days of the item"""
        return self._last_90_days
