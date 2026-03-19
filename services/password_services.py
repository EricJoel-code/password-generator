from core.generator import PasswordGenerator
from security.entropy import PasswordEntropy
from core.passphrase_generator import PassphraseGenerator
from security.breach_checker import BreachChecker


class PasswordService:

    def create_password(
        self, lenght: int, lowercase=True, uppercase=True, digits=True, symbols=False
    ):

        charset = PasswordGenerator.get_charset(lowercase, uppercase, digits, symbols)

        password = PasswordGenerator.generate(lenght, charset)

        entropy = PasswordEntropy.calculate_entropy(password)

        strength = PasswordEntropy.strength_label(entropy)

        is_weak = BreachChecker.is_weak(password)

        return {
            "password": password,
            "entropy": entropy,
            "strength": strength,
            "is_weak": is_weak,
        }

    def create_passphrase(self, words: int = 4):

        passphrase = PassphraseGenerator.generate(words)

        entropy = PasswordEntropy.calculate_entropy(passphrase)

        strength = PasswordEntropy.strength_label(entropy)

        is_weak = BreachChecker.is_weak(passphrase)

        return {
            "password": passphrase,
            "entropy": entropy,
            "strength": strength,
            "is_weak": is_weak,
        }
