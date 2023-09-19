def has_numbers(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False

def caesar_cipher(text: str, key: int, action: str) -> any:
    result: str = ''

    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    updated_text: str = text.upper().replace(" ", "")

    for char in updated_text:
        if 'A' <= char <= 'Z':
            if action == "encryption":
                encrypted_char = alphabet[(alphabet.index(char) + key) % 26]
                result += encrypted_char
            elif action == "decryption":
                decrypted_char = alphabet[(alphabet.index(char) - key) % 26]
                result += decrypted_char
        else:
            print("The text must contain only letters from 'A' to 'Z'.")
            return ""

    return result


if __name__ == "__main__":
    key: int = int(input("Enter the key (between 1 and 25): "))
    if key < 1 or key > 25:
        raise ValueError("The key must be between 1 and 25.")

    action: str = input("Choose the operation (encryption/decryption): ").lower()
    if not (action == "encryption" or action == "decryption"):
        raise ValueError("Operation must be encryption or decryption")

    text: str = input("Enter the text: ")
    if has_numbers(text):
        raise ValueError("Text has numbers")

    if action == "encryption":
        result: str = caesar_cipher(text, key, "encryption")
        print("The ciphertext is:", result)
    elif action == "decryption":
        result: str = caesar_cipher(text, key, "decryption")
        print("The decrypted message is:", result)
