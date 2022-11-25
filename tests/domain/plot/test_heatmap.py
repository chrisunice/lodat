import pytest
import lodat as lo


@pytest.fixture(scope='function')
def data_object(test_assets_path):
    return lo.DataObject(f"{test_assets_path}\\test_data.csv")


def test_heatmap(data_object):

    heatmap = lo.plot.Heatmap()