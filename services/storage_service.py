import os


class StorageService:

    @staticmethod
    def save_file(upload_file):

        path = os.path.join(
            "uploads",
            upload_file.filename
        )

        with open(path, "wb") as file:
            file.write(upload_file.file.read())

        return path