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

from .color import Color
from .enums import AppID, Currency, SaleType

__all__ = ("Tag", "SaleFeedSale", "SaleFeed", "Sticker")


class Tag:
    __slots__ = (
        "_name",
        "_name_localized",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._name = data.get("name", "")
        self._name_localized = data.get("name_localized", "")

    def __repr__(self) -> str:
        return f"Tag(data={{'name': {self._name}, 'name_localized': {self._name_localized}}})"

    def __str__(self) -> str:
        return self._name

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, str):
            return self._name == __o or self._name_localized == __o
        elif isinstance(__o, Tag):
            return self._name == __o._name or self._name_localized == __o._name_localized
        return False

    @property
    def name(self) -> str:
        """:class:`str`: Returns the name of the item."""
        return self._name

    @property
    def name_localized(self) -> str:
        """:class:`str`: Returns the localized name of the item."""
        return self._name_localized


class Sticker:
    __slots__ = (
        "_color",
        "_img",
        "_name",
        "_name_localized",
        "_slot",
        "_sticker_id",
        "_type",
        "_type_localized",
        "_wear",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._color = data.get("color")
        self._img = data.get("img")
        self._name = data.get("name")
        self._name_localized = data.get("name_localized")
        self._slot = data.get("slot")
        self._sticker_id = data.get("sticker_id")
        self._type = data.get("type")
        self._type_localized = data.get("type_localized")
        self._wear = data.get("wear")

    @property
    def color(self) -> Optional[Color]:
        """:class:`Color`: Returns the color of the sticker."""
        return Color(self._color) if self._color is not None else None

    @property
    def img(self) -> str:
        """:class:`str`: Returns the image URL of the sticker."""
        return self._img

    @property
    def name(self) -> str:
        """:class:`str`: Returns the name of the sticker."""
        return self._name

    @property
    def name_localized(self) -> str:
        """:class:`str`: Returns the localized name of the sticker."""
        return self._name_localized

    @property
    def slot(self) -> int:
        """:class:`int`: Returns the slot of the sticker."""
        return self._slot

    @property
    def sticker_id(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the sticker ID of the sticker."""
        return self._sticker_id

    @property
    def type(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the type of the sticker."""
        return self._type

    @property
    def type_localized(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the localized type of the sticker."""
        return self._type

    @property
    def wear(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the wear of the sticker."""
        return self._wear


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

    def __repr__(self) -> str:
        return f"<SaleFeedSale marketHashName={self._marketHashName} salePrice={self._salePrice} currency={self._currency}>"

    def __str__(self) -> str:
        return self._marketHashName

    @property
    def id_(self) -> int:
        """:class:`int`: Returns the ID of the sale feed event."""
        return self._id

    @property
    def sale_id(self) -> int:
        """:class:`int`: Returns the ID of the sale."""
        return self._saleId

    @property
    def product_id(self) -> int:
        """:class:`int`: Returns the ID of the product."""
        return self._productId

    @property
    def asset_id(self) -> int:
        """:class:`int`: Returns the ID of the asset."""
        return self._assetId

    @property
    def item_id(self) -> int:
        """:class:`int`: Returns the ID of the item."""
        return self._itemId

    @property
    def app_id(self) -> AppID:
        """:class:`int`: Returns the ID of the app."""
        return AppID(self._appid)

    @property
    def steam_id(self) -> str:
        """:class:`str`: Returns the Steam ID of Skinport bot which holds the item."""
        return self._steamid

    @property
    def url(self) -> str:
        """:class:`str`: Returns the listing URL of the item."""
        match self.app_id:
            case AppID.tf2:
                return f"https://skinport.com/tf2/item/{self._url}/{self._saleId}"
            case AppID.dota2:
                return f"https://skinport.com/dota2/item/{self._url}/{self._saleId}"
            case AppID.rust:
                return f"https://skinport.com/rust/item/{self._url}/{self._saleId}"
            case _:
                return f"https://skinport.com/item/{self._url}/{self._saleId}"

    @property
    def family(self) -> str:
        """:class:`str`: Returns the family of the item."""
        return self._family

    @property
    def family_localized(self) -> str:
        """:class:`str`: Returns the localized family of the item."""
        return self._family_localized

    @property
    def name(self) -> str:
        """:class:`str`: Returns the name of the item."""
        return self._name

    @property
    def title(self) -> str:
        """:class:`str`: Returns the title of the item."""
        return self._title

    @property
    def text(self) -> str:
        """:class:`str`: Returns additional text of the item."""
        return self._text

    @property
    def market_name(self) -> str:
        """:class:`str`: Returns the name of the item under it is displayed on skinport.com."""
        return self._marketName

    @property
    def market_hash_name(self) -> str:
        """:class:`str`: Returns the name of the item under it is displayed on skinport.com."""
        return self._marketHashName

    @property
    def color(self) -> Color:
        """:class:`Color`: Returns the color of the item."""
        return Color(self._color)

    @property
    def bg_color(self) -> Optional[Color]:
        """Optional[:class:`Color`]: Returns the background color of the item."""
        return self._bgColor if self._bgColor is not None else None

    @property
    def image(self) -> str:
        """:class:`str`: Returns link to the item image."""
        return f"https://community.cloudflare.steamstatic.com/economy/image/{self._image}"

    @property
    def classid(self) -> str:
        return self._classid

    @property
    def assetid(self) -> str:
        return self._assetid

    @property
    def lock(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the time until the item is trade-locked."""
        return datetime.datetime.strptime(self._lock, "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def version(self) -> str:
        """:class:`str`: Returns the item version."""
        return self._version

    @property
    def version_type(self) -> str:
        """:class:`str`: Returns the type of the item version."""
        return self._versionType

    @property
    def stack_able(self) -> bool:
        """:class:`bool`: Indicates if the item is stackable."""
        return self._stackAble

    @property
    def suggested_price(self) -> float:
        """:class:`float`: Returns the suggested sale price of the item."""
        return self._suggestedPrice / 100

    @property
    def sale_price(self) -> float:
        """:class:`float`: Returns the sale price of the item."""
        return self._salePrice / 100

    @property
    def currency(self) -> Currency:
        """:class:`Currency`: Returns the currency of the item."""
        return Currency(self._currency)

    @property
    def sale_status(self) -> str:
        """:class:`str`: Returns the sale status of the item."""
        return self._saleStatus

    @property
    def sale_type(self) -> SaleType:
        """:class:`SaleType`: Returns the sale type."""
        return SaleType(self._saleType)

    @property
    def category(self) -> str:
        """:class:`str`: Returns the category of the item."""
        return self._category

    @property
    def category_localized(self) -> str:
        """:class:`str`: Returns the localized category of the item."""
        return self._category_localized

    @property
    def sub_category(self) -> Optional[str]:
        """:class:`str`: Returns the sub category of the item."""
        return self._subCategory

    @property
    def sub_category_localized(self) -> Optional[str]:
        """:class:`str`: Returns the localized sub category of the item."""
        return self._subCategory_localized

    @property
    def pattern(self) -> Optional[int]:
        """Optional[:class:`int`]: Returns the pattern seed of the item."""
        return self._pattern

    @property
    def finish(self) -> Optional[int]:
        """Optional[:class:`int`]: Returns the finish seed of the item."""
        return self._finish

    @property
    def custom_name(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the name tag of the item."""
        return self._customName

    @property
    def wear(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the wear of the item."""
        return self._wear

    @property
    def link(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the link of the item to view it in-game."""
        return self._link

    @property
    def type(self) -> str:
        """:class:`str`: Returns the type of the item."""
        return self._type

    @property
    def exterior(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the exterior of the item."""
        return self._exterior

    @property
    def rarity(self) -> str:
        """:class:`str`: Returns the rarity of the item."""
        return self._rarity

    @property
    def rarity_localized(self) -> str:
        """:class:`str`: Returns the localized rarity of the item."""
        return self._rarity_localized

    @property
    def rarity_color(self) -> Color:
        """:class:`Color`: Returns the color of the rarity."""
        return Color(self._rarityColor)

    @property
    def collection(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the collection of the item."""
        return self._collection

    @property
    def collection_localized(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the localized collection of the item."""
        return self._collection_localized

    @property
    def stickers(self) -> List[Sticker]:
        """List[:class:`str`]: Returns a :class:`list` of :class:`str` with names of attached stickers. Can be empty."""
        return [Sticker(data=sticker) for sticker in self._stickers]

    @property
    def can_have_screenshots(self) -> bool:
        """:class:`bool`: Indicates if the item can have screenshots."""
        return self._canHaveScreenshots

    @property
    def screenshots(self) -> List[str]:
        """List[:class:`str`]: Returns a :class:`list` of :class:`str` of available screenshots. Can be empty."""
        return self._screenshots

    @property
    def souvenir(self) -> bool:
        """:class:`bool`: Indicates if the item is of Souvenir quality."""
        return self._souvenir

    @property
    def stattrak(self) -> bool:
        """:class:`bool`: Indicates if the item is of StatTrak™ quality."""
        return self._stattrak

    @property
    def tags(self) -> List[Tag]:
        """List[:class:`Tag`]: Returns a :class:`list` of :class:`Tag`."""
        return [Tag(data=tag) for tag in self._tags]

    @property
    def own_item(self) -> bool:
        """:class:`bool`: Indicates if the item is your own."""
        return self._ownItem


class SaleFeed:
    __slots__ = (
        "_event_type",
        "_sales",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._event_type = data.get("eventType", "")
        self._sales = data.get("sales", [])

    def __repr__(self) -> str:
        return f"<SaleFeed event_type={self._event_type}>"

    @property
    def event_type(self) -> str:
        """:class:`str`: Returns the type of the event."""
        return self._event_type

    @property
    def sales(self) -> List[SaleFeedSale]:
        """List[:class:`SaleFeedSale`]: Returns a :class:`list` of :class:`SaleFeedSale`."""
        return [SaleFeedSale(data=sale) for sale in self._sales]
