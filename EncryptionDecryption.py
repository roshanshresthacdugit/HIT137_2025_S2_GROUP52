class EncryptionDecryption:


    def __init__(self, shift1: int, shift2: int):
        self.shift1 = shift1
        self.shift2 = shift2
        self.shift1_mul_shift2 = self.shift1 * self.shift2
        self.shift1_add_shift2 = self.shift1 + self.shift2

def main():
    while True:
        try:
            shift1 = int(input("Enter the first shift value: "))
            shift2 = int(input("Enter the second shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    enc_dec = EncryptionDecryption(shift1, shift2)
    