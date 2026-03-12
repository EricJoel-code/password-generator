import secrets


class PassphraseGenerator:

    WORD_LIST = [
        "forest",
        "rocket",
        "coffee",
        "galaxy",
        "ladder",
        "island",
        "pencil",
        "dragon",
        "planet",
        "silver",
        "shadow",
        "castle",
        "river",
        "ocean",
        "tiger",
        "cloud",
        "desert",
        "falcon",
        "stone",
        "thunder",
    ]

    @classmethod
    def generate(cls, num_words: int = 4, separator: str = "-"):

        words = [secrets.choice(cls.WORD_LIST) for _ in range(num_words)]

        return separator.join(words)
