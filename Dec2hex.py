import sys

def decimal_to_hex(decimal_value):
    """Convert a decimal number to its hexadecimal representation."""
    
    if not isinstance(decimal_value, int):  # Ensure input is an integer
        return "Error: Input must be an integer."

    hex_chars = '0123456789ABCDEF'
    hexadecimal = ""

    if decimal_value == 0:
        return "0"

    num = decimal_value
    while num > 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    return hexadecimal

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Error: No input provided. Usage: python Dec2Hex.py <integer>")
        sys.exit(1)  # Exit with error code

    try:
        decimal_value = int(sys.argv[1])  # Convert input to integer
        print(f"Hexadecimal: {decimal_to_hex(decimal_value)}")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
