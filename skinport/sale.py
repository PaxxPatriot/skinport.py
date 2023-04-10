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
from typing import Any, Dict, Optional

__all__ = (
    "Sale",
    "LastXDays",
)


class Sale:
    """Represents a sale."""

    __slots__ = (
        "_price",
        "_wear_value",
        "_sold_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._price: float = data.get("price", 0.0)
        self._wear_value: Optional[float] = data.get("wear_value")
        self._sold_at = data.get("sold_at", 0)

    def __repr__(self) -> str:
        return f"Sale({{'price': {self._price}, 'wear_value': {self._wear_value}, 'sold_at': {self._sold_at}}})"

    @property
    def price(self) -> float:
        """:class:`float`: Returns the price of the item."""
        return self._price

    @property
    def wear_value(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the wear value of the item."""
        return self._wear_value

    @property
    def sold_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the date and time the item was sold."""
        return datetime.datetime.fromtimestamp(self._sold_at)


class LastXDays:
    __slots__ = (
        "_min",
        "_max",
        "_avg",
        "_volume",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._min = data.get("min")
        self._max = data.get("max")
        self._avg = data.get("avg")
        self._volume: int = data.get("volume", 0)

    def __repr__(self) -> str:
        return f"LastXDays({{'min': {self._min}, 'max': {self._max}, 'avg': {self._avg}, 'volume': {self._volume}}}"

    @property
    def min(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the min of the last x days"""
        return self._min

    @property
    def max(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the max of the last x days"""
        return self._max

    @property
    def avg(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the avg of the last x days"""
        return self._avg

    @property
    def volume(self) -> int:
        """:class:`int`: Returns the volume of the last x days"""
        return self._volume
