import unittest

from Stock import Stock


class TestJamStocks(unittest.TestCase):

    def test_add_stock(self):
        stock = Stock()
        stock.add("MLK")
        value = stock.find("MLK")

        self.assertEqual(value, True)

    def test_remove_stock(self):
        stock = Stock()
        stock.add("MLK")
        value = stock.remove("MLK")

        self.assertEqual(value, True)

if __name__ == '__main__':
    unittest.main()
