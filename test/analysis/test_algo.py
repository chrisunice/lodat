import pytest
import lodat as lo
import pandas as pd


@pytest.fixture
def data_objects(test_assets_path):
    test = lo.DataObject(f"{test_assets_path}\\test_data.csv")
    base = lo.DataObject(f"{test_assets_path}\\baseline_data.csv")
    return [test, base]


def test_load(data_objects):
    algo = lo.Algo(*data_objects)
    assert isinstance(algo, lo.Algo)


def test_analyze_normal(data_objects):
    algo = lo.Algo(*data_objects)
    results = algo.analyze(10000, 'VV', bootstrap=False)
    assert isinstance(results, pd.DataFrame)


def test_analyze_strapped(data_objects):
    algo = lo.Algo(*data_objects)
    results = algo.analyze(10000, 'VV', bootstrap=True)
    assert isinstance(results, pd.DataFrame)
