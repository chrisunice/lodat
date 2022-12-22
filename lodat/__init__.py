import os
from configparser import ConfigParser

config = ConfigParser()
config.read(f"{os.path.dirname(__file__)}\\config.ini")

from lodat.data import DataObject
from lodat.analysis import Algo
from lodat import stats
from lodat import utils
from lodat import plots
from lodat.database.manager import ImageryDatabaseManager
