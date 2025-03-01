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

__all__ = ("Color",)

from typing import Tuple, Union


class Color:
    """Represents a Skinport color. This class is similar to a (red, green, blue) :class:`tuple`.

    Attributes
    ------------
    value: :class:`int`
        The raw integer colour value.
    """

    __slots__ = ("value",)

    def __init__(self, value: Union[int, str]) -> None:
        if isinstance(value, str):
            self.value: int = int(value[1:], 16) if value.startswith("#") else int(value, 16)
        elif isinstance(value, int):
            self.value: int = value

    def _get_byte(self, byte: int) -> int:
        return (self.value >> (8 * byte)) & 0xFF

    def __str__(self) -> str:
        return f"#{self.value:0>6x}"

    def __int__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f"Color(value={self.value!r})"

    def __hash__(self) -> int:
        return hash(self.value)

    @property
    def r(self) -> int:
        """:class:`int`: Returns the red component of the colour."""
        return self._get_byte(2)

    @property
    def g(self) -> int:
        """:class:`int`: Returns the green component of the colour."""
        return self._get_byte(1)

    @property
    def b(self) -> int:
        """:class:`int`: Returns the blue component of the colour."""
        return self._get_byte(0)

    def to_rgb(self) -> Tuple[int, int, int]:
        """Tuple[:class:`int`, :class:`int`, :class:`int`]: Returns an (r, g, b) tuple representing the colour."""
        return (self.r, self.g, self.b)
