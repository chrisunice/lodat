from pymongo import MongoClient
import lodat as lo


class DatabaseManager:
    def __init__(self, platform: str):
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client.get_database(platform)



if __name__ == '__main__':

    dbm = DatabaseManager('Platform')