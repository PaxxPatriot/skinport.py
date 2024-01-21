import json
import unittest

from skinport import Currency, ItemOutOfStock, ItemWithSales

TEST_SALES = """[
  {
    "market_hash_name": "Glove Case Key",
    "currency": "EUR",
    "item_page": "https://skinport.com/item/glove-case-key",
    "market_page": "https://skinport.com/market/730?cat=Key&item=Glove+Case+Key",
    "sales": [
      {
        "price": 1.77,
        "wear_value": null,
        "sold_at": 1568005548
      },
      {
        "price": 1.77,
        "wear_value": null,
        "sold_at": 1567816819
      },
      {
        "price": 1.77,
        "wear_value": null,
        "sold_at": 1567816819
      }
    ],
    "last_7_days": {
      "min": 1.77,
      "max": 1.95,
      "avg": 1.81,
      "volume": 4
    },
    "last_30_days": {
      "min": 1.77,
      "max": 2.03,
      "avg": 1.93,
      "volume": 59
    },
    "last_90_days": {
      "min": 1.77,
      "max": 2.03,
      "avg": 1.93,
      "volume": 68
    }
  },
  {
    "market_hash_name": "★ Karambit | Slaughter (Minimal Wear)",
    "item_page": "https://skinport.com/item/karambit-slaughter-minimal-wear",
    "market_page": "https://skinport.com/market/730?cat=Knife&type=Karambit&item=Slaughter",
    "currency": "EUR",  
    "sales": [
      {
        "price": 250,
        "wear_value": 0.13740462064743042,
        "sold_at": 1565526086
      },
      {
        "price": 300,
        "wear_value": 0.07707387208938599,
        "sold_at": 1562708712
      }
    ],
    "last_7_days": {
      "min": null,
      "max": null,
      "avg": null,
      "volume": 0
    },
    "last_30_days": {
      "min": 250,
      "max": 250,
      "avg": 250,
      "volume": 1
    },
    "last_90_days": {
      "min": 250,
      "max": 300,
      "avg": 275,
      "volume": 2
    }
  }
]
"""
TEST_OUT_OF_STOCK = """[
    {
        "market_hash_name": "Souvenir AWP | Desert Hydra (Factory New)",
        "version": null,
        "currency": "EUR",
        "suggested_price": 9995.66,
        "avg_sale_price": 6287.45,
        "sales_last_90d": 6
    },
    {
        "market_hash_name": "★ Butterfly Knife | Gamma Doppler (Factory New)",
        "version": "Emerald",
        "currency": "EUR",
        "suggested_price": 15110.53,
        "avg_sale_price": 11786.21,
        "sales_last_90d": 2
    },
    {
        "market_hash_name": "★ Sport Gloves | Vice (Factory New)",
        "version": null,
        "currency": "EUR",
        "suggested_price": 26309.29,
        "avg_sale_price": 22484.59,
        "sales_last_90d": 1
    },
    {
        "market_hash_name": "★ Sport Gloves | Pandora's Box (Minimal Wear)",
        "version": null,
        "currency": "EUR",
        "suggested_price": 9099.2,
        "avg_sale_price": 5762.36,
        "sales_last_90d": 3
    }
]"""


class SaleTestCase(unittest.TestCase):
    def setUp(self):
        self._out_of_stock = json.loads(TEST_OUT_OF_STOCK)
        self._sales = json.loads(TEST_SALES)

    def test_sales_constructor(self):
        sales = [ItemWithSales(data=data) for data in self._sales]
        self.assertEqual(len(sales), 2)
        self.assertEqual(sales[0].market_hash_name, "Glove Case Key")
        self.assertEqual(sales[0].currency, Currency.eur)
        self.assertEqual(
            sales[0].item_page,
            "https://skinport.com/item/glove-case-key",
        )
        self.assertEqual(
            sales[0].market_page,
            "https://skinport.com/market/730?cat=Key&item=Glove+Case+Key",
        )
        self.assertTrue(len(sales[0].sales) > 0)
        self.assertEqual(sales[0].last_7_days.min, 1.77)
        self.assertEqual(sales[0].last_7_days.max, 1.95)
        self.assertEqual(sales[0].last_7_days.avg, 1.81)
        self.assertEqual(sales[0].last_7_days.volume, 4)
        self.assertEqual(sales[0].last_30_days.min, 1.77)
        self.assertEqual(sales[0].last_30_days.max, 2.03)
        self.assertEqual(sales[0].last_30_days.avg, 1.93)
        self.assertEqual(sales[0].last_30_days.volume, 59)
        self.assertEqual(sales[0].last_90_days.min, 1.77)
        self.assertEqual(sales[0].last_90_days.max, 2.03)
        self.assertEqual(sales[0].last_90_days.avg, 1.93)
        self.assertEqual(sales[0].last_90_days.volume, 68)

    def test_out_of_stock_constructor(self):
        out_of_stock = [ItemOutOfStock(data=data) for data in self._out_of_stock]
        self.assertEqual(len(out_of_stock), 4)
        self.assertEqual(
            out_of_stock[0].market_hash_name,
            "Souvenir AWP | Desert Hydra (Factory New)",
        )
        self.assertEqual(out_of_stock[0].version, None)
        self.assertEqual(out_of_stock[0].currency, Currency.eur)
        self.assertEqual(out_of_stock[0].suggested_price, 9995.66)
        self.assertEqual(out_of_stock[0].avg_sale_price, 6287.45)
        self.assertEqual(out_of_stock[0].sales_last_90d, 6)
