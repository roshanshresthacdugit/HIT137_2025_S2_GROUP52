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
    
    def encrypt(self, text: str) -> str:
        """Encrypt the input text."""
        result = []
        for char in text:
            if 'a' <= char <= 'm':
                result.append(self.shift_char(char, self.shift1_mul_shift2, 'a', 'm'))
            elif 'n' <= char <= 'z':
                result.append(self.shift_char(char, -(self.shift1_add_shift2), 'n', 'z'))
            elif 'A' <= char <= 'M':
                result.append(self.shift_char(char, -self.shift1, 'A', 'M'))
            elif 'N' <= char <= 'Z':
                result.append(self.shift_char(char, self.shift2**2, 'N', 'Z'))
            else:
                result.append(char)
        return "".join(result)
    
    def decrypt(self, text: str) -> str:
        """Decrypt the input text."""
        result = []
        for char in text:
            if 'a' <= char <= 'm':
                result.append(self.shift_char(char, -(self.shift1_mul_shift2), 'a', 'm'))
            elif 'n' <= char <= 'z':
                result.append(self.shift_char(char, self.shift1_add_shift2, 'n', 'z'))
            elif 'A' <= char <= 'M':
                result.append(self.shift_char(char, self.shift1, 'A', 'M'))
            elif 'N' <= char <= 'Z':
                result.append(self.shift_char(char, -(self.shift2**2), 'N', 'Z'))
            else:
                result.append(char)
        return "".join(result)

 
    def verify_decryption(self, original_text: str, decrypted_text: str) -> bool:
        """Verify if the decrypted text is identical to the original."""
        return original_text == decrypted_text
 

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
    raw_text = "raw_text.txt"
    encrypted_file_name = "encrypted_text.txt"
    decrypted_file_name = "decrypted_text.txt"

    try:
         with open(raw_text, 'r') as f:
            text = f.read()
    except FileNotFoundError:
            print("Error: 'raw_text.txt' not found. Please create the file and try again.")
            return
    
    print("\n--- Encryption Started ---")
    encrypted = enc_dec.encrypt(text)
    with open(encrypted_file_name, 'w') as f:
        f.write(encrypted)
    print(f"Encrypted file saved as '{encrypted_file_name}'")
    
    print("\n--- Decryption Started ---")
    decrypted = enc_dec.decrypt(encrypted)
    with open(decrypted_file_name, 'w') as f:
        f.write(decrypted)
    print(f"Decrypted file saved as '{decrypted_file_name}'")

    print("\n--- Verification ---")
    if enc_dec.verify_decryption(text, decrypted):
      print("Verification successful: The decrypted text matches the original.")
    else:
         print("Verification failed: The decrypted text does not match the original.")
 
 


if __name__ == "__main__":
    main()
