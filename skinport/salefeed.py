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

__all__ = ("Tag", "SaleFeedSale", "SaleFeed")


class Tag:

    __slots__ = (
        "_name",
        "_name_localized",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._name = data.get("name", "")
        self._name_localized = data.get("name_localized", "")

    @property
    def name(self) -> str:
        return self._name

    @property
    def name_localized(self) -> str:
        return self._name_localized


class SaleFeedSale:

    __slots__ = (
        "_id",
        "_saleId",
        "_productId",
        "_assetId",
        "_itemId",
        "_appid",
        "_steamid",
        "_url",
        "_family",
        "_family_localized",
        "_name",
        "_title",
        "_text",
        "_marketName",
        "_marketHashName",
        "_color",
        "_bgColor",
        "_image",
        "_classid",
        "_assetid",
        "_lock",
        "_version",
        "_versionType",
        "_stackAble",
        "_suggestedPrice",
        "_salePrice",
        "_currency",
        "_saleStatus",
        "_saleType",
        "_category",
        "_category_localized",
        "_subCategory",
        "_subCategory_localized",
        "_pattern",
        "_finish",
        "_customName",
        "_wear",
        "_link",
        "_type",
        "_exterior",
        "_rarity",
        "_rarity_localized",
        "_rarityColor",
        "_collection",
        "_collection_localized",
        "_stickers",
        "_canHaveScreenshots",
        "_screenshots",
        "_souvenir",
        "_stattrak",
        "_tags",
        "_ownItem",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._id = data.get("id", 0)
        self._saleId = data.get("saleId", 0)
        self._productId = data.get("productId", 0)
        self._assetId = data.get("assetId", 0)
        self._itemId = data.get("itemId", 0)
        self._appid = data.get("appid", 0)
        self._steamid = data.get("steamid", "")
        self._url = data.get("url", "")
        self._family = data.get("family", "")
        self._family_localized = data.get("family_localized", "")
        self._name = data.get("name", "")
        self._title = data.get("title", "")
        self._text = data.get("text", "")
        self._marketName = data.get("marketName", "")
        self._marketHashName = data.get("marketHashName", "")
        self._color = data.get("color", "")
        self._bgColor = data.get("bgColor")
        self._image = data.get("image", "")
        self._classid = data.get("classid", "")
        self._assetid = data.get("assetid", "")
        self._lock = data.get("lock", "")
        self._version = data.get("version", "")
        self._versionType = data.get("versionType", "")
        self._stackAble = data.get("stackAble", False)
        self._suggestedPrice = data.get("suggestedPrice", 0)
        self._salePrice = data.get("salePrice", 0)
        self._currency = data.get("currency", "")
        self._saleStatus = data.get("saleStatus", "")
        self._saleType = data.get("saleType", "")
        self._category = data.get("category", "")
        self._category_localized = data.get("category_localized", "")
        self._subCategory = data.get("subCategory")
        self._subCategory_localized = data.get("subCategory_localized")
        self._pattern = data.get("pattern")
        self._finish = data.get("finish")
        self._customName = data.get("customName")
        self._wear = data.get("wear")
        self._link = data.get("link")
        self._type = data.get("type", "")
        self._exterior = data.get("exterior")
        self._rarity = data.get("rarity", "")
        self._rarity_localized = data.get("rarity_localized", "")
        self._rarityColor = data.get("rarityColor", "")
        self._collection = data.get("collection")
        self._collection_localized = data.get("collection_localized")
        self._stickers = data.get("stickers", [])
        self._canHaveScreenshots = data.get("canHaveScreenshots", False)
        self._screenshots = data.get("screenshots", [])
        self._souvenir = data.get("souvenir", False)
        self._stattrak = data.get("stattrak", False)
        self._tags = data.get("tags", [])
        self._ownItem = data.get("ownItem", False)

    @property
    def id_(self) -> int:
        return self._id

    @property
    def sale_id(self) -> int:
        return self._saleId

    @property
    def product_id(self) -> int:
        return self._productId

    @property
    def asset_id(self) -> int:
        return self._assetId

    @property
    def item_id(self) -> int:
        return self._itemId

    @property
    def app_id(self) -> int:
        return self._appid

    @property
    def steam_id(self) -> str:
        return self._steamid

    @property
    def url(self) -> str:
        return self._url

    @property
    def family(self) -> str:
        return self._family

    @property
    def family_localized(self) -> str:
        return self._family_localized

    @property
    def name(self) -> str:
        return self._name

    @property
    def title(self) -> str:
        return self._title

    @property
    def text(self) -> str:
        return self._text

    @property
    def market_name(self) -> str:
        return self._marketName

    @property
    def market_hash_name(self) -> str:
        return self._marketHashName

    @property
    def color(self) -> str:
        return self._color

    @property
    def bg_color(self) -> Optional[str]:
        return self._bgColor

    @property
    def image(self) -> str:
        return self._image

    @property
    def classid(self) -> str:
        return self._classid

    @property
    def assetid(self) -> str:
        return self._assetid

    @property
    def lock(self) -> datetime.datetime:
        return datetime.datetime.strptime(self._lock, "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def version(self) -> str:
        return self._version

    @property
    def version_type(self) -> str:
        return self._versionType

    @property
    def stack_able(self) -> bool:
        return self._stackAble

    @property
    def suggested_price(self) -> int:
        return self._suggestedPrice

    @property
    def sale_price(self) -> int:
        return self._salePrice

    @property
    def currency(self) -> Currency:
        return Currency(self._currency)

    @property
    def sale_status(self) -> str:
        return self._saleStatus

    @property
    def sale_type(self) -> str:
        return self._saleType

    @property
    def category(self) -> str:
        return self._category

    @property
    def category_localized(self) -> str:
        return self._category_localized

    @property
    def sub_category(self) -> Optional[str]:
        return self._subCategory

    @property
    def sub_category_localized(self) -> Optional[str]:
        return self._subCategory_localized

    @property
    def pattern(self) -> Optional[str]:
        return self._pattern

    @property
    def finish(self) -> Optional[str]:
        return self._finish

    @property
    def custom_name(self) -> Optional[str]:
        return self._customName

    @property
    def wear(self) -> Optional[str]:
        return self._wear

    @property
    def link(self) -> Optional[str]:
        return self._link

    @property
    def type(self) -> str:
        return self._type

    @property
    def exterior(self) -> Optional[str]:
        return self._exterior

    @property
    def rarity(self) -> str:
        return self._rarity

    @property
    def rarity_localized(self) -> str:
        return self._rarity_localized

    @property
    def rarity_color(self) -> str:
        return self._rarityColor

    @property
    def collection(self) -> Optional[str]:
        return self._collection

    @property
    def collection_localized(self) -> Optional[str]:
        return self._collection_localized

    @property
    def stickers(self) -> List[str]:
        return self._stickers

    @property
    def can_have_screenshots(self) -> bool:
        return self._canHaveScreenshots

    @property
    def screenshots(self) -> List[str]:
        return self._screenshots

    @property
    def souvenir(self) -> bool:
        return self._souvenir

    @property
    def stattrak(self) -> bool:
        return self._stattrak

    @property
    def tags(self) -> List[Tag]:
        return [Tag(data=tag) for tag in self._tags]

    @property
    def own_item(self) -> bool:
        return self._ownItem


class SaleFeed:

    __slots__ = (
        "_event_type",
        "_sales",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._event_type = data.get("eventType", "")
        self._sales = data.get("sales", [])

    @property
    def event_type(self) -> str:
        return self._event_type

    @property
    def sales(self) -> List[SaleFeedSale]:
        return [SaleFeedSale(data=sale) for sale in self._sales]
