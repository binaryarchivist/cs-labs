alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Ă Ș Ț Â Î'.split(' ')


class Vigenere:
    def __init__(self, text: str, key: str):
        self.original_text = text
        self.key = key
        self.parsed_text = ''.join([char for char in text.upper() if not char.isspace()])

    def encrypt(self) -> str:
        encrypted = []

        for i in range(len(self.parsed_text)):
            c = self.parsed_text[i]
            c_index = alphabet.index(c)
            key_c_index = alphabet.index(self.key[i % len(self.key)])
            new_c_index = (c_index + key_c_index) % len(alphabet)
            encrypted_c = alphabet[new_c_index]

            encrypted.append(encrypted_c)

        return ''.join(encrypted)

    def decrypt(self) -> str:
        decrypted = []

        for i in range(len(self.parsed_text)):
            c = self.parsed_text[i]
            c_index = alphabet.index(c)
            key_c_index = alphabet.index(self.key[i % len(self.key)])
            new_c_index = (c_index - key_c_index + len(alphabet)) % len(alphabet)
            decrypted_c = alphabet[new_c_index]

            decrypted.append(decrypted_c)

        return ''.join(decrypted)

    @staticmethod
    def validate_text(text: str):
        return all(char.upper() in alphabet or char.isspace() for char in text)

    @staticmethod
    def is_valid_key(key: str):
        return all(c in alphabet for c in key)
