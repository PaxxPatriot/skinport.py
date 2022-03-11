import json
import unittest

from skinport import SaleFeed, SaleFeedSale, Tag

TEST_SALEFEED = """{
    "eventType": "listed",
    "sales": [
        {
            "id": 0,
            "saleId": 6934215,
            "productId": 5544725,
            "assetId": 55034907,
            "itemId": 61019,
            "appid": 730,
            "steamid": "76561198837215063",
            "url": "driver-gloves-rezan-the-red-well-worn",
            "family": "Rezan the Red",
            "family_localized": "Rezan the Red",
            "name": "Rezan the Red",
            "title": "Driver Gloves",
            "text": "Well-Worn ★ Extraordinary Gloves",
            "marketName": "★ Driver Gloves | Rezan the Red (Well-Worn)",
            "marketHashName": "★ Driver Gloves | Rezan the Red (Well-Worn)",
            "color": "#8650AC",
            "bgColor": null,
            "image": "-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAX1R3LjtQurWzLhRfwP_BcjZ9_tmslY60mvLwOq7cqWdQ-sJ0xLCTpt6l0AawrkNvajz7LdXDJFJtMguBqwfokrvn0cC0upTAmCdru3Q8pSGKBwn68BM",
            "classid": "4142171394",
            "assetid": "24958657824",
            "lock": "2022-02-27T08:00:00.000Z",
            "version": "default",
            "versionType": "default",
            "stackAble": false,
            "suggestedPrice": 10004,
            "salePrice": 7903,
            "currency": "EUR",
            "saleStatus": "listed",
            "saleType": "public",
            "category": "Gloves",
            "category_localized": "Gloves",
            "subCategory": "Driver Gloves",
            "subCategory_localized": "Driver Gloves",
            "pattern": 990,
            "finish": 10069,
            "customName": null,
            "wear": 0.3809339106082916,
            "link": "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198837215063A24958657824D11533664215916898619",
            "type": "★ Extraordinary Gloves",
            "exterior": "Well-Worn",
            "quality": "★",
            "rarity": "Extraordinary",
            "rarity_localized": "Extraordinary",
            "rarityColor": "#eb4b4b",
            "collection": null,
            "collection_localized": null,
            "stickers": [],
            "canHaveScreenshots": true,
            "screenshots": [],
            "souvenir": false,
            "stattrak": false,
            "tags": [
                {
                    "name": "Well-Worn",
                    "name_localized": "Well-Worn"
                },
                {
                    "name": "★",
                    "name_localized": "★"
                },
                {
                    "name": "Gloves",
                    "name_localized": "Gloves"
                },
                {
                    "name": "Extraordinary",
                    "name_localized": "Extraordinary"
                }
            ],
            "ownItem": false
        }
    ]
}
"""


class SalefeedTestCase(unittest.TestCase):
    def setUp(self):
        self._sale_feed = json.loads(TEST_SALEFEED)

    def test_sale_feed_constructor(self):
        sale_feed = SaleFeed(data=self._sale_feed)
        self.assertIsInstance(sale_feed, SaleFeed)
