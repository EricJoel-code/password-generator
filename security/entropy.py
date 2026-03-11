import math


class PasswordEntropy:

    @staticmethod
    def calculate_entropy(password: str) -> float:

        charset_size = 0

        if any(c.islower() for c in password):
            charset_size += 26

        if any(c.isupper() for c in password):
            charset_size += 26

        if any(c.isdigit() for c in password):
            charset_size += 10

        if any(not c.isalnum() for c in password):
            charset_size += 32

        if charset_size == 0:
            return 0

        entropy = len(password) * math.log2(charset_size)

        return round(entropy, 2)

    @staticmethod
    def strength_label(entropy: str) -> str:
        if entropy < 40:
            return "Débil"

        elif entropy < 60:
            return "Media"

        elif entropy < 80:
            return "Fuerte"

        else:
            return "Muy fuerte"
