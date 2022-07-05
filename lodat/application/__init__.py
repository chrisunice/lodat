from configparser import ConfigParser


class Configuration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('./config.ini')

        # Adding all config.ini content as attributes
        for section_name, section in self.config.items():
            for key, value in section.items():
                if not hasattr(self, key):
                    setattr(self, key, value)


config = Configuration()
