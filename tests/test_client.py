import datetime
import unittest

import skinport

from skinport import AuthenticationError, Currency

import config


class SkinportTestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = skinport.Client()

    async def test_get_items(self):
        await self.client.get_items()

    async def test_get_items_with_currency(self):
        items = await self.client.get_items(currency=Currency.cny)
        self.assertIsInstance(items[0].currency, Currency)

    async def test_get_items_datetime(self):
        items = await self.client.get_items()
        self.assertIsInstance(items[0].created_at, datetime.datetime)

    async def test_get_sales_history(self):
        await self.client.get_sales_history(
            market_hash_name=["Yeti Coated Wrench (Minimal Wear)"]
        )

    async def test_get_sales_out_of_stock(self):
        await self.client.get_sales_out_of_stock()

    async def test_get_account_transactions(self):
        with self.assertRaises(AuthenticationError):
            await self.client.get_account_transactions()

    async def test_get_account_inventory(self):
        self.client.set_auth(
            client_id=config.client_id, client_secret=config.client_secret
        )
        await self.client.get_account_transactions()

    async def asyncTearDown(self):
        await self.client.close()
