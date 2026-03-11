from core.generator import PasswordGenerator
from security.entropy import PasswordEntropy


class PasswordService:

    def create_password(
        self, lenght: int, lowercase=True, uppercase=True, digits=True, symbols=False
    ):

        charset = PasswordGenerator.get_charset(lowercase, uppercase, digits, symbols)

        password = PasswordGenerator.generate(lenght, charset)

        entropy = PasswordEntropy.calculate_entropy(password)

        strength = PasswordEntropy.strength_label(entropy)

        return {"password": password, "entropy": entropy, "strength": strength}
