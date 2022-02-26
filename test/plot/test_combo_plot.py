import pytest
from lodat.analysis import Algo
from lodat.plot import ComboPlot
from lodat.data import DataObject


@pytest.fixture
def result(test_assets_path):
    test = DataObject(f"{test_assets_path}\\test_data.csv")
    base = DataObject(f"{test_assets_path}\\baseline_data.csv")
    algo = Algo(test, base)
    result = algo.analyze(10000, 'VV', True)
    return result


def test_combo_plot(result):
    upper_data = result.loc[2.5]
    cp = ComboPlot(upper_data)
    success = cp.render()
    assert success


