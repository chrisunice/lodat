import pytest
import lodat as lo


@pytest.fixture
def result(test_assets_path):
    test = lo.DataObject(f"{test_assets_path}\\test_data.csv")
    base = lo.DataObject(f"{test_assets_path}\\baseline_data.csv")
    algo = lo.Algo(test, base)
    result = algo.analyze(10000, 'VV', True)
    return result


def test_combo_plot(result):
    upper_data = result.loc[2.5]
    cp = lo.plot.ComboPlot(upper_data, title='')
    success = cp.render()
    assert success


