import pandas as pd
import pytest
import numpy as np
from lodat.stats.outliers import fences


@pytest.fixture
def my_list():
    return list(range(10))


def test_fences(my_list):
    my_outlier = 10000
    my_list.append(my_outlier)
    arr = np.array(my_list)
    interval = fences(arr, coverage_factor=1.5)
    assert max(interval) < my_outlier


def test_fences_dims():
    arr_2d = np.random.random(size=(10, 10))
    with pytest.raises(AssertionError):
        fences(arr_2d)


def test_list_type(my_list):
    interval = fences(my_list)
    assert isinstance(interval, tuple)


def test_array_type(my_list):
    my_arr = np.array(my_list)
    interval = fences(my_arr)
    assert isinstance(interval, tuple)


def test_series_type(my_list):
    my_series = pd.Series(my_list)
    interval = fences(my_series)
    assert isinstance(interval, tuple)
