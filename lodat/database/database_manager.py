import sqlite3
from . import Configuration


class DatabaseManager(Configuration):
    def __init__(self):
        super().__init__()
        self.database_path = self.config['DEFAULT']['imagery_database_path']
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()

        self.initialize_database()

    def initialize_database(self):
        try:
            sql_statement = "CREATE TABLE data (" \
                            "ImagePath TEXT," \
                            "Band TEXT INDEX," \
                            "Polarization TEXT," \
                            "Look INTEGER," \
                            "Depression INTEGER," \
                            "Author TEXT," \
                            "Autoprocessed INTEGER," \
                            "Date TEXT," \
                            "Platform TEXT," \
                            "Source TEXT)"
            self.cursor.execute(sql_statement)
            self.conn.commit()
        except Exception as e:
            print(e)

        return True

    def purge_database(self):
        # todo code to remove all tables
        pass

    def close_database(self):
        """ Tear down method """
        self.cursor.close()
        self.conn.close()
        return True

    def __del__(self):
        return self.close_database()
