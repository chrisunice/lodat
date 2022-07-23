import pandas as pd
import pytest
import numpy as np

import lodat as lo


@pytest.fixture
def my_list():
    return list(range(10))


def test_fences(my_list):
    my_outlier = 10000
    my_list.append(my_outlier)
    arr = np.array(my_list)
    interval = lo.stats.fences(arr, coverage_factor=1.5)
    assert max(interval) < my_outlier


def test_fences_dims():
    arr_2d = np.random.random(size=(10, 10))
    with pytest.raises(AssertionError):
        lo.stats.fences(arr_2d)


def test_list_type(my_list):
    interval = lo.stats.fences(my_list)
    assert isinstance(interval, tuple)


def test_array_type(my_list):
    my_arr = np.array(my_list)
    interval = lo.stats.fences(my_arr)
    assert isinstance(interval, tuple)


def test_series_type(my_list):
    my_series = pd.Series(my_list)
    interval = lo.stats.fences(my_series)
    assert isinstance(interval, tuple)
