import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(decimal_to_hex(15), "F")
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_zero_input(self):
        self.assertEqual(decimal_to_hex(0), "0")

    def test_large_number(self):
        self.assertEqual(decimal_to_hex(1024), "400")

if __name__ == "__main__":
    unittest.main()

