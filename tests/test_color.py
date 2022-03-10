import unittest

from skinport import Color


class ColorTestCase(unittest.TestCase):
    def test_color_constructor_with_hashtag(self):
        color = Color("#eb4b4b")

        self.assertEqual(color.value, 0xEB4B4B)

    def test_color_constructor_without_hashtag(self):
        color = Color("eb4b4b")

        self.assertEqual(color.value, 0xEB4B4B)

    def test_color_constructor_without_hashtag(self):
        color = Color(0xEB4B4B)

        self.assertEqual(color.value, 0xEB4B4B)

    def test_r(self):
        color = Color("#eb4b4b")

        self.assertEqual(color.r, 235)

    def test_g(self):
        color = Color("#eb4b4b")

        self.assertEqual(color.g, 75)

    def test_b(self):
        color = Color("#eb4b4b")

        self.assertEqual(color.b, 75)

    def test_str(self):
        color = Color("#eb4b4b")

        self.assertEqual(str(color), "#eb4b4b")
        self.assertEqual(repr(color), "<Color value=15420235>")
