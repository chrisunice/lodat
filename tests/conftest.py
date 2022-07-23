import pytest


@pytest.fixture(scope='package')
def test_assets_path():
    return r"C:\LODAT\test_assets"
