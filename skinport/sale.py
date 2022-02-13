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
from typing import Optional

__all__ = (
    "Sale",
    "LastXDays",
)


class Sale:
    """Represents a sale."""

    __slots__ = (
        "_price",
        "_wear_value",
        "_sale_at",
    )

    def __init__(self, *, data) -> None:
        self._price = data.get("price")
        self._wear_value = data.get("wear_value")
        self._sale_at = datetime.datetime.fromtimestamp(data.get("sale_at"))

    def __repr__(self) -> str:
        return f"Sale({{'price': {self._price}, 'wear_value': {self._wear_value}, 'sale_at': {self._sale_at}}})"

    def __str__(self) -> str:
        return f"{self._id}"

    @property
    def price(self) -> float:
        """Returns the price of the item."""
        return self._price

    @property
    def wear_value(self) -> Optional[float]:
        """Returns the wear value of the item."""
        return self._wear_value

    @property
    def sale_at(self) -> datetime.datetime:
        """Returns the date and time the item was sold."""
        return self._sale_at


class LastXDays:

    __slots__ = (
        "_min",
        "_max",
        "_avg",
        "_volume",
    )

    def __init__(self, *, data) -> None:
        self._min = data.get("min")
        self._max = data.get("max")
        self._avg = data.get("avg")
        self._volume = data.get("volume")

    def __repr__(self) -> str:
        return f"LastXDays({{'min': {self._min}, 'max': {self._max}, 'avg': {self._avg}, 'volume': {self._volume}}}"

    def __str__(self) -> str:
        return f"Min: {self._min} - Max: {self._max} - Avg: {self._avg} - Volume: {self._volume}"

    @property
    def min(self) -> Optional[float]:
        """:class:`str` Returns the min of the last x days"""
        return self._min

    @property
    def max(self) -> Optional[float]:
        """:class:`str` Returns the max of the last x days"""
        return self._max

    @property
    def avg(self) -> Optional[float]:
        """:class:`str` Returns the avg of the last x days"""
        return self._avg

    @property
    def volume(self) -> int:
        """:class:`str` Returns the volume of the last x days"""
        return self._volume
