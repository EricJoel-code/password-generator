import os


class BreachChecker:

    FILE_PATH = "data/rockyou.txt"
    _passwords_cache = None

    # Umbral (en bytes) para decidir estrategia
    MAX_MEMORY_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    @classmethod
    def load_passwords(cls):

        if cls._passwords_cache is None:

            if not os.path.exists(cls.FILE_PATH):
                cls._passwords_cache = set()
                return cls._passwords_cache

            file_size = os.path.getsize(cls.FILE_PATH)

            # Si el archivo es pequeño -> cargar en memoria
            if file_size <= cls.MAX_MEMORY_FILE_SIZE:

                with open(
                    cls.FILE_PATH, "r", encoding="latin-1", errors="ignore"
                ) as file:
                    cls._passwords_cache = set(
                        line.strip().lower() for line in file if line.strip()
                    )
            else:
                # Archivo grande -> no usar cache
                cls._passwords_cache = None

        return cls._passwords_cache

    @classmethod
    def is_weak(cls, password: str) -> bool:

        password = password.lower()

        # Intentar usar cache
        passwords = cls.load_passwords()

        if passwords is not None:
            return password in passwords

        # 🔥 STREAMING MODE (archivo grande)
        if not os.path.exists(cls.FILE_PATH):
            return False

        with open(cls.FILE_PATH, "r", encoding="latin-1", errors="ignore") as file:
            for line in file:
                if password == line.strip().lower():
                    return True

        return False
