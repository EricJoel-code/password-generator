import string
import secrets


class PasswordGenerator:

    @staticmethod
    def generate(length: int, charset: str) -> str:
        return "".join(secrets.choice(charset) for _ in range(length))

    @staticmethod
    def get_charset(lowercase=True, uppercase=True, digits=True, symbols=False) -> str:

        charset = ""

        if lowercase:
            charset += string.ascii_lowercase

        if uppercase:
            charset += string.ascii_uppercase

        if digits:
            charset += string.digits

        if symbols:
            charset += string.punctuation

        if not charset:
            raise ValueError("Debe seleccionar al menos un tipo de caracter")

        return charset
