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

from enum import Enum, IntEnum

__all__ = (
    "Currency",
    "AppID",
    "Locale",
    "SaleType",
    "Exterior",
)


class Currency(Enum):
    aud = "AUD"
    brl = "BRL"
    cad = "CAD"
    chf = "CHF"
    cny = "CNY"
    czk = "CZK"
    dkk = "DKK"
    eur = "EUR"
    gbp = "GBP"
    hrk = "HRK"
    nok = "NOK"
    pln = "PLN"
    rub = "RUB"
    sek = "SEK"
    try_ = "TRY"
    usd = "USD"

    def __str__(self) -> str:
        return self.value


class AppID(IntEnum):
    csgo = 730
    dota2 = 570
    rust = 252490
    tf2 = 440


class Locale(Enum):
    en = "en"
    de = "de"
    ru = "ru"
    fr = "fr"
    zh = "zh"
    nl = "nl"
    fi = "fi"
    es = "es"
    tr = "tr"

    def __str__(self) -> str:
        return self.value


class SaleType(Enum):
    public = "public"
    private = "private"

    def __str__(self) -> str:
        return self.value


class Exterior(Enum):
    factory_new = "Factory New"
    minimal_wear = "Minimal Wear"
    field_tested = "Field-Tested"
    well_worn = "Well-Worn"
    battle_scarred = "Battle-Scarred"

    def __str__(self) -> str:
        return self.value
