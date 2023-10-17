from Vigenere import Vigenere

MIN_KEY_LENGTH = 3

text: str = input("Text (no symbols/digits, any case, space allowed) = ")

while not text or not Vigenere.validate_text(text):
    text = input("Invalid text, input again: ")

key: str = input("Key (uppercase, no whitespace) = ")

while not key or len(key) < MIN_KEY_LENGTH or not Vigenere.is_valid_key(key):
    key = input("Invalid key, input again: ")

operation = input("Operation, input 'decrypt' or 'encrypt' = ")

while not operation or (operation != 'encrypt' and operation != 'decrypt'):
    operation = input("Invalid operation, input again: ")

vigenere = Vigenere(text, key)

if operation == 'decrypt':
    print(f"Decrypted text: {vigenere.decrypt()}")
elif operation == 'encrypt':
    print(f"Encrypted text: {vigenere.encrypt()}")
