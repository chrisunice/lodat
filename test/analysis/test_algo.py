import pytest
import pandas as pd
from lodat.analysis import Algo
from lodat.data import DataObject


@pytest.fixture
def data_objects(test_assets_path):
    test = DataObject(f"{test_assets_path}\\test_data.csv")
    base = DataObject(f"{test_assets_path}\\baseline_data.csv")
    return [test, base]


def test_load(data_objects):
    algo = Algo(*data_objects)
    assert isinstance(algo, Algo)


def test_analyze_normal(data_objects):
    algo = Algo(*data_objects)
    results = algo.analyze(10000, 'VV', bootstrap=False)
    assert isinstance(results, pd.DataFrame)


def test_analyze_strapped(data_objects):
    algo = Algo(*data_objects)
    results = algo.analyze(10000, 'VV', bootstrap=True)
    assert isinstance(results, pd.DataFrame)
