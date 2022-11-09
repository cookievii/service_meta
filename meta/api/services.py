import os


class Meta:
    @staticmethod
    def get_time(path: str, file_name: str = "") -> float:
        """Возвращает время последней модификации файла или каталога"""
        time = os.path.getmtime(path + file_name)
        return time

    @staticmethod
    def get_type(path: str, file_name: str = "") -> str:
        """Возвращает "file" если path указывает на файл, folder" если папка."""
        is_file = os.path.isfile(path + file_name)
        if is_file:
            return "file"
        return "folder"


def path_exists(path: str) -> bool:
    """Возвращает True, если путь ссылается на существующий путь"""
    if os.path.exists(path):
        return True
    return False


def get_contents_from_path(path: str) -> dict:
    """Возвращает список с метаданными файлов по указанной директории"""
    path_contents = {"data": []}

    contents = os.listdir(path)
    for content in contents:
        path_contents["data"].append(
            {
                "name": content,
                "type": Meta.get_type(path, content),
                "time": Meta.get_time(path, content),
            }
        )
    return path_contents
