from core.generator import PasswordGenerator


class PasswordService:

    def create_password(
        self, lenght: int, lowercase=True, uppercase=True, digits=True, symbols=False
    ):

        charset = PasswordGenerator.get_charset(lowercase, uppercase, digits, symbols)

        password = PasswordGenerator.generate(lenght, charset)

        return password
