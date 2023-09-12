def caesar_cipher_with_two_keys(text: str, key1: int, key2: str, action: str) -> any:
    result: str = ""

    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    updated_text: str = text.upper().replace(" ", "")

    index_key2: int = 0

    for char in updated_text:
        if 'A' <= char <= 'Z':
            if action == "encryption":
                key = (key1 + ord(key2[index_key2 % len(key2)].upper()) - ord('A')) % 26

                encrypted_char = alphabet[(alphabet.index(char) + key) % 26]
                result += encrypted_char

                index_key2 += 1
            elif action == "decryption":
                key = (key1 + ord(key2[index_key2 % len(key2)].upper()) - ord('A')) % 26

                decrypted_char = alphabet[(alphabet.index(char) - key) % 26]
                result += decrypted_char

                index_key2 += 1
        else:
            raise ValueError("The text must contain only letters from 'A' to 'Z'.")

    return result


if __name__ == "__main__":
    key1: int = int(input("Enter key 1 (between 1 and 25): "))
    if key1 < 1 or key1 > 25:
        raise ValueError("Key 1 must be between 1 and 25.")

    key2: str = input("Enter key 2 (at least 7 letters of the English alphabet): ")
    if not (key2.isalpha() and len(key2) >= 7):
        raise ValueError(
            "Key 2 must contain only letters of the English alphabet and have a minimum length of 7 characters.")

    action: str = input("Choose the operation (encryption/decryption): ").lower()
    if action == "encryption" or action == "decryption":
        print()
    else:
        raise ValueError("Operation must be encryption or decryption")

    text: str = input("Enter the text: ")

    if action == "encryption":
        result: str = caesar_cipher_with_two_keys(text, key1, key2, "encryption")
        print("The ciphertext is:", result)
    elif action == "decryption":
        result: str = caesar_cipher_with_two_keys(text, key1, key2, "decryption")
        print("The decrypted message is:", result)
