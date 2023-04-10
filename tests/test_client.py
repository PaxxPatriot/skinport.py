import asyncio
import datetime
import sys
import unittest
from typing import Optional

import config

import skinport
from skinport import AuthenticationError, Currency, ParamRequired


class SkinportClientTestCase(unittest.IsolatedAsyncioTestCase):
    def run(self, result: Optional[unittest.TestResult] = None):
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        return super().run(result)

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
        await self.client.get_sales_history()

    async def test_get_sales_out_of_stock(self):
        await self.client.get_sales_out_of_stock()

    async def test_get_account_transactions(self):
        with self.assertRaises(AuthenticationError):
            await self.client.get_account_transactions()

    async def test_get_account_inventory(self):
        self.client.set_auth(client_id=config.client_id, client_secret=config.client_secret)
        await self.client.get_account_transactions()

    async def asyncTearDown(self):
        await self.client.close()
