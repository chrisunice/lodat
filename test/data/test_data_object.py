from lodat.data import DataObject


def test_raw_data(test_assets_path):
    obj = DataObject(f"{test_assets_path}\\test_data.csv")
    assert not obj.raw_data.empty


def test_data(test_assets_path):
    obj = DataObject(f"{test_assets_path}\\test_data.csv")
    assert bool(obj.data)


