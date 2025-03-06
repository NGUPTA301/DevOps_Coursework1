import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(0), "")  # Edge case

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_hex("ABC")  # Invalid string input
        with self.assertRaises(TypeError):
            decimal_to_hex(10.5)  # Float input
        with self.assertRaises(TypeError):
            decimal_to_hex(None)  # NoneType input

if __name__ == "__main__":
    unittest.main()
