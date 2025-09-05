"""
Question1: Encryption, Decryption and Verification 
=============================================================================
This program encrypts and decrypts text using two user-provided shift values.
It reads input text from 'raw_text.txt', saves the encrypted version to
'encrypted_text.txt', and the decrypted version to 'decrypted_text.txt'.
Finally, it verifies that the decrypted text matches the original.
"""

class EncryptionDecryption:

    """
    A class to handle custom encryption and decryption operations
    based on two integer shift values.
    """

    def __init__(self, shift1: int, shift2: int):
        self.shift1 = shift1
        self.shift2 = shift2
        self.shift1_mul_shift2 = self.shift1 * self.shift2
        self.shift1_add_shift2 = self.shift1 + self.shift2

    def shift_char(self, char: str, shift: int, start: str, end: str) -> str:
        """Shift a character within a defined range using arithmetic expression."""
        base = ord(start)
        size = ord(end) - ord(start) + 1
        return chr((ord(char) - base + shift) % size + base)

def main():

    """Main function to handle user input, encryption, decryption, and verification."""
    while True:
        try:
            shift1 = int(input("Enter the first shift value: "))
            shift2 = int(input("Enter the second shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    enc_dec = EncryptionDecryption(shift1, shift2)


if __name__ == "__main__":
    main()
