from datetime import datetime
import os


class FileStorage:

    FILE_PATH = "data/passwords.txt"

    @classmethod
    def save_password(cls, password):

        os.makedirs("data", exist_ok=True)

        with open(cls.FILE_PATH, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file.write(f"{timestamp} | {password}\n")
