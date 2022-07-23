import os
import pytest


@pytest.fixture(scope='package')
def test_assets_path():
    return r"C:\LODAT\test_assets"


@pytest.fixture(scope='package')
def save_path():
    this_dir = os.path.dirname(__file__)
    plot_dir = f"{this_dir}\\plots"
    try:
        os.mkdir(plot_dir)
    except FileExistsError:
        pass
    return plot_dir
