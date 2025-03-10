import pytest
from Dec2Hex import decimal_to_hex

def test_valid_conversion():
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(255) == "FF"
    assert decimal_to_hex(0) == "0"

def test_invalid_input():
    assert decimal_to_hex("abc") == "Error: Input must be an integer."
    assert decimal_to_hex(None) == "Error: Input must be an integer."
    assert decimal_to_hex(3.14) == "Error: Input must be an integer."

def test_large_number():
    assert decimal_to_hex(4095) == "FFF"

if __name__ == "__main__":
    pytest.main()
