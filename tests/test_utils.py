import unittest

import skinport


class UtilsTestCase(unittest.TestCase):
    def test_market_hash_name_awp(self):
        market_hash_name = skinport.utils.market_hash_name("AWP | BOOM", skinport.Exterior.factory_new)
        self.assertEqual(market_hash_name, "AWP | BOOM (Factory New)")

    def test_market_hash_name_knife(self):
        market_hash_name = skinport.utils.market_hash_name("★ Bowie Knife | Crimson Web", skinport.Exterior.factory_new)
        self.assertEqual(market_hash_name, "★ Bowie Knife | Crimson Web (Factory New)")
