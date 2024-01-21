import datetime
import json
import unittest

from skinport import Currency, Item

TEST_ITEMS = """[
  {
    "market_hash_name": "AK-47 | Aquamarine Revenge (Battle-Scarred)",
    "currency": "EUR",  
    "suggested_price": 13.18,
    "item_page": "https://skinport.com/item/ak-47-aquamarine-revenge-battle-scarred",
    "market_page": "https://skinport.com/market/730?cat=Rifle&item=Aquamarine+Revenge",
    "min_price": 11.33,
    "max_price": 18.22,
    "mean_price": 12.58,
    "quantity": 25,
    "created_at": 1535988253,
    "updated_at": 1568073728
  },
  {
    "market_hash_name": "★ M9 Bayonet | Fade (Factory New)",
    "currency": "EUR",
    "suggested_price": 319.11,
    "item_page": "https://skinport.com/item/m9-bayonet-fade-factory-new",
    "market_page": "https://skinport.com/market/730?cat=Knife&item=Fade",
    "min_price": null,
    "max_price": null,
    "mean_price": null,
    "quantity": 0,
    "created_at": 1535988302,
    "updated_at": 1568073725
  }
]"""


class ItemTestCase(unittest.TestCase):
    def setUp(self):
        self._items = json.loads(TEST_ITEMS)

    def test_item_constructor(self):
        items = [Item(data=data) for data in self._items]
        self.assertEqual(len(items), 2)
        self.assertEqual(
            items[0].market_hash_name,
            "AK-47 | Aquamarine Revenge (Battle-Scarred)",
        )
        self.assertEqual(items[0].currency, Currency.eur)
        self.assertEqual(items[0].suggested_price, 13.18)
        self.assertEqual(
            items[0].item_page,
            "https://skinport.com/item/ak-47-aquamarine-revenge-battle-scarred",
        )
        self.assertEqual(
            items[0].market_page,
            "https://skinport.com/market/730?cat=Rifle&item=Aquamarine+Revenge",
        )
        self.assertEqual(items[0].min_price, 11.33)
        self.assertEqual(items[0].max_price, 18.22)
        self.assertEqual(items[0].mean_price, 12.58)
        self.assertEqual(items[0].quantity, 25)
        self.assertEqual(
            items[0].created_at,
            datetime.datetime.fromtimestamp(1535988253),
        )
        self.assertEqual(
            items[0].updated_at,
            datetime.datetime.fromtimestamp(1568073728),
        )

    def test_item_str(self):
        items = [Item(data=data) for data in self._items]
        self.assertEqual(str(items[0]), "AK-47 | Aquamarine Revenge (Battle-Scarred)")

    def test_item_repr(self):
        items = [Item(data=data) for data in self._items]
        self.assertEqual(
            repr(items[0]),
            "<Item market_hash_name=AK-47 | Aquamarine Revenge (Battle-Scarred) market_page=https://skinport.com/market/730?cat=Rifle&item=Aquamarine+Revenge quantity=25>",
        )
