import lodat as lo
from pymongo import MongoClient

if __name__ == '__main__':

    db = MongoClient(host='localhost', port=27017)

    dot = lo.DataObject(r"C:\LODAT\test_assets\test_data.csv")

    # TODO need to make some more fake data in LODAT folder