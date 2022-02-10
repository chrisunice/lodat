import os
from configparser import ConfigParser


class Configuration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(f"{os.path.dirname(__file__)}\\config.ini")
