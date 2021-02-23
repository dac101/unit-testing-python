import unittest

from Stock import Stock


class TestJamStock(unittest.TestCase):

    def test_add_stock(self):
        stock = Stock()
        stock.add("MLK")
        value = stock.find("MLK")

        self.assertEqual(value, False)