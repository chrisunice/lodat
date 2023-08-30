# Building config
import json
import os.path

path_to_config = f"{os.path.dirname(__file__)}\\config.json"
with open(path_to_config, mode='r') as json_file:
    config = json.load(json_file)

# Package specific imports
from lodat.data import DataObject
from lodat.analysis import Algo
from lodat import stats
from lodat import utils
from lodat import plots
from lodat.database.manager import ImageryDatabaseManager
