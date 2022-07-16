import os
from configparser import ConfigParser


class Configuration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(f"{os.path.dirname(__file__)}\\config.ini")

from .domain.data import DataObject
from .domain.analysis import Algo
from .domain import stats
from .domain import utils
from .domain import plot
from .database.manager import ImageryDatabaseManager
