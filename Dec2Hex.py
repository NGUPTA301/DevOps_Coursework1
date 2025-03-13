import sys

def decimal_to_hex(decimal_value):
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    if num == 0:
        return "0"  # Edge case for zero input

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) < 2:  # No input provided
        print("Error: No input argument provided. Usage: python Dec2Hex.py <decimal_number>")
        sys.exit(1)  # Exit with an error code

    try:
        decimal_value = int(sys.argv[1])  # Convert input to integer
        if decimal_value < 0:
            print("Error: Please provide a non-negative integer.I just updated the description")
            sys.exit(1)  # Exit for negative numbers
        decimal_to_hex(decimal_value)
    except ValueError:
        print("Error: Please provide a valid integer.I am going to push it")
        sys.exit(1)  # Exit with an error code
