import sqlite3
import pandas as pd
from lodat.application import config


class ImageryDatabaseManager:
    def __init__(self, path_to_database=None):
        # Establish connection
        if path_to_database is None:
            path_to_database = config.imagery_database_path
        self.conn = sqlite3.connect(path_to_database)
        self.cursor = self.conn.cursor()
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

    def query(self, platforms: list, bands: list, polarizations: list,
              look_min: int, look_max: int, depr_min: float, depr_max: float):

        # Note hard coded the first element just to get it working
        sql_statement = "SELECT * FROM data WHERE " \
                        f"Platform == '{platforms[0]}' AND " \
                        f"Band == '{bands[0]}' AND " \
                        f"Polarization == '{polarizations[0]}' AND " \
                        f"Look >= {look_min} AND Look <= {look_max} AND " \
                        f"Depression >= {depr_min} AND Depression <= {depr_max}"

        return pd.read_sql(sql_statement, self.conn)

    def close(self):
        self.cursor.close()
        self.conn.close()
        return True
