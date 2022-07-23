from lodat import Configuration


def test_config():
    config = Configuration()
    assert hasattr(config, 'config')