import unittest

import skinport


class SkinportTestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = skinport.Client()
        await self.client.login()

    async def test_get_items(self):
        await self.client.get_items()

    async def test_get_sales_history(self):
        await self.client.get_sales_history(market_hash_name=["Yeti Coated Wrench (Minimal Wear)"])

    async def test_get_sales_out_of_stock(self):
        await self.client.get_sales_out_of_stock()

    async def asyncTearDown(self):
        await self.client.close()
