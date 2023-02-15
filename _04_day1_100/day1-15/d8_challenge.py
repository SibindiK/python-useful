# encrypt text by shifting each character position up by a shift amount
def encrypt(alphabet, message, shift):
    encryption = ""
    for char in message:
        position = alphabet.index(char)
        encryption += alphabet[position + shift]
    return encryption


# decrypt text by shifting each character position down by a shift amount
def decipher(alphabet, message, shift):
    decryption = ""
    for char in message:
        position = alphabet.index(char)
        decryption += alphabet[position - shift]
    return decryption


def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt or 'decode to decrypt:'\n")
    text = input("Enter message:\n").lower()
    shift = int(input("Enter shift: "))
    if direction == "encode":
        print(f"Your encoded message is: {encrypt(alphabet, text, shift)}")
        #encrypt(alphabet, text, shift)
    elif direction == "decode":
        print(f"Decoded message is: {decipher(alphabet, text, shift)}")


if __name__ == "__main__":
    main()
