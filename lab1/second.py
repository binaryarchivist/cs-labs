def has_numbers(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False


def generate_modified_alphabet(key2):
    key2 = ''.join(sorted(set(key2.upper()), key=key2.upper().index))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    modified_alphabet = key2 + \
                        ''.join(filter(lambda char: char not in key2, alphabet))
    print(f'Modified alphabet: {modified_alphabet}')
    return modified_alphabet

def caesar_cipher_with_two_keys(text: str, key1: int, key2: str, action: str) -> any:
    result: str = ""

    alphabet: str = generate_modified_alphabet(key2)

    updated_text: str = text.upper().replace(" ", "")

    for char in updated_text:
        if char in alphabet:
            new_index = 0
            index = alphabet.index(char)
            if action == 'encryption':
                new_index = (index + key1) % len(alphabet)
            elif action == 'decryption':
                new_index = (index - key1 + len(alphabet)) % len(alphabet)
            result += alphabet[new_index]
        else:
            return 'Only English alphabet characters (A-Z) are allowed.'

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
    if not (action == "encryption" or action == "decryption"):
        raise ValueError("Operation must be encryption or decryption")

    text: str = input("Enter the text: ")

    if has_numbers(text):
        raise ValueError("Text has numbers")

    if action == "encryption":
        result: str = caesar_cipher_with_two_keys(text, key1, key2, "encryption")
        print("The ciphertext is:", result)
    elif action == "decryption":
        result: str = caesar_cipher_with_two_keys(text, key1, key2, "decryption")
        print("The decrypted message is:", result)
