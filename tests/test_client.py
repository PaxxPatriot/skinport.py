import unittest

import skinport


class SkinportTestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = skinport.Client()
        await self.client.login()

    async def test_get_items(self):
        await self.client.get_items()

    async def asyncTearDown(self):
        await self.client.close()
