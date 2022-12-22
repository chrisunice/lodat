import lodat as lo
from configparser import ConfigParser


def test_config():
    assert isinstance(lo.config, ConfigParser)
