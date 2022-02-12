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

from skinport.enums import Currency


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
        self._sale_at = data.get("sale_at")

    def __repr__(self) -> str:
        return f"Sale({{'price': {self._price}, 'wear_value': {self._wear_value}, 'sale_at': {self._sale_at}}})"

    def __str__(self) -> str:
        return f"{self._id}"

    @property
    def id(self) -> Optional[int]:
        """:class:`int` Returns the id of the sale"""
        return self._id

    @property
    def type(self) -> str:
        """:class:`str` Returns the type of the sale"""
        return self._type

    @property
    def sub_type(self) -> str:
        """:class:`str` Returns the sub type of the sale"""
        return self._sub_type

    @property
    def status(self) -> str:
        """:class:`str` Returns the status of the sale"""
        return self._status

    @property
    def amount(self) -> float:
        """:class:`str` Returns the amount of the sale"""
        return self._amount

    @property
    def fee(self) -> Optional[float]:
        """:class:`str` Returns the fee of the sale"""
        return self._fee

    @property
    def currency(self) -> Currency:
        """:class:`str` Returns the currency of the sale"""
        return self._currency

    @property
    def items(self) -> list:
        """:class:`list` Returns the items of the sale"""
        return self._items

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`str` Returns the created at of the sale"""
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        """:class:`str` Returns the updated at of the sale"""
        return self._updated_at


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
    def min(self) -> float:
        """:class:`str` Returns the min of the last x days"""
        return self._min

    @property
    def max(self) -> float:
        """:class:`str` Returns the max of the last x days"""
        return self._max

    @property
    def avg(self) -> float:
        """:class:`str` Returns the avg of the last x days"""
        return self._avg

    @property
    def volume(self) -> float:
        """:class:`str` Returns the volume of the last x days"""
        return self._volume
