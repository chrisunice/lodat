import sqlite3
from lodat.application import config


class ImageryDatabaseManager:
    def __init__(self, path_to_database=None):
        # Establish connection
        if path_to_database is None:
            path_to_database = config.imagery_database_path
        self.dbm = sqlite3.connect(path_to_database)
        self.cursor = self.dbm.cursor()
        self.cursor.row_factory = lambda _, row: row[0]

        # Metadata
        self.platforms = self._get_platforms()
        self.bands = self._get_bands()
        self.polarizations = self._get_polarizations()

    def _get_platforms(self):
        return self.cursor.execute("SELECT DISTINCT Platform from data ORDER BY Platform").fetchall()

    def _get_bands(self):
        return self.cursor.execute("SELECT DISTINCT Band from data ORDER BY Band").fetchall()

    def _get_polarizations(self):
        return self.cursor.execute("SELECT DISTINCT Polarization from data ORDER BY Polarization").fetchall()

    def close(self):
        self.cursor.close()
        self.dbm.close()
        return True

    def __del__(self):
        self.close()
