"""Convert a base-32 number (digits 0-9, A-V) to octal using dictionaries. """

# base-32 digit -> 5-bit binary string
BASE32_TO_BINARY = {
    "0": "00000", "1": "00001", "2": "00010", "3": "00011",
    "4": "00100", "5": "00101", "6": "00110", "7": "00111",
    "8": "01000", "9": "01001", "A": "01010", "B": "01011",
    "C": "01100", "D": "01101", "E": "01110", "F": "01111",
    "G": "10000", "H": "10001", "I": "10010", "J": "10011",
    "K": "10100", "L": "10101", "M": "10110", "N": "10111",
    "O": "11000", "P": "11001", "Q": "11010", "R": "11011",
    "S": "11100", "T": "11101", "U": "11110", "V": "11111",
}

# 3-bit binary string -> octal digit
BINARY_TO_OCTAL = {
    "000": "0", "001": "1", "010": "2", "011": "3",
    "100": "4", "101": "5", "110": "6", "111": "7",
}


def base32_to_octal(base32_number):
    """Return the octal string for a valid base-32 string."""
    # Step 1: base-32 digits -> one long binary string
    bits = ""
    for digit in base32_number:
        bits += BASE32_TO_BINARY[digit]

    # Step 2: left-pad with zeros so the length is a multiple of 3
    remainder = len(bits) % 3
    if remainder != 0:
        bits = "0" * (3 - remainder) + bits

    # Step 3: every 3 bits -> one octal digit
    octal = ""
    for i in range(0, len(bits), 3):
        octal += BINARY_TO_OCTAL[bits[i:i + 3]]

    # Step 4: drop leading zeros (but keep a single 0 for a zero value)
    octal = octal.lstrip("0")
    return octal if octal else "0"


def main():
    user_input = input("Enter a base-32 number (digits 0-9, A-V): ").strip().upper()

    if user_input == "":
        print("Error: no input entered.")
        return

    # Validate using the dictionary itself
    for digit in user_input:
        if digit not in BASE32_TO_BINARY:
            print(f"Error: '{digit}' is not a valid base-32 digit (use 0-9 and A-V).")
            return

    print(f"Octal: {base32_to_octal(user_input)}")


if __name__ == "__main__":
    main()
