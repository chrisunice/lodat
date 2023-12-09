import os
import shutil
import fnmatch
import tempfile
from pathlib import Path


class CipherPrepper:
    def __init__(self, ignore_file: str):
        self.ignore_file = ignore_file
        self.ignore_patterns = self._get_ignore_patterns()

        self.temp_dir = tempfile.mkdtemp(dir='C:\\')

    def _get_ignore_patterns(self):
        with open(self.ignore_file, mode='r') as file:
            ignore_patterns = file.read().splitlines()
        return ignore_patterns

    def is_ignored(self, item, directory):
        item = '/' + str(item.relative_to(directory))
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(item, pattern):
                return True
        return False

    @staticmethod
    def is_human_readable(file_path):
        try:
            with open(file_path, mode='r') as file:
                preview = file.read(4096)
                return all(c.isprintable() or c.isspace() for c in preview)
        except Exception:
            return False

    def walk(self, directory: str):
        # Walk down a directory and files
        root = Path(directory)
        for item in root.iterdir():

            if self.is_ignored(item, directory):
                # Skip ignored items
                continue

            if item.is_dir():
                self.walk(str(item))
            else:
                if self.is_human_readable(str(item)):
                    shutil.copy(str(item), self.temp_dir)

        os.startfile(self.temp_dir)
        return self.temp_dir


if __name__ == '__main__':
    project_dir_path = os.path.dirname(os.path.dirname(__file__))

    ignore_file_path = f"{project_dir_path}\\scratches\\.cipherignore"
    prepper = CipherPrepper(ignore_file_path)

    folder = prepper.walk(project_dir_path)
