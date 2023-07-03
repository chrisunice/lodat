from lodat.data.fast_data_object import FastDataObject


def test_fast_dot(test_assets_path):
    path_to_data = f"{test_assets_path}\\test_data.csv"
    fast_dot = FastDataObject(path_to_data)
    assert True
