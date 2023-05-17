import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    # возвращает корректный путь до файла
    return os.path.join(FILES_DIR, filename)


CSV_FILE = get_path(filename="books.csv")
JSON_FILE = get_path(filename='users.json')
