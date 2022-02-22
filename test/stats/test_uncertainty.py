import pytest
import numpy as np
import pandas as pd
from lodat.stats.uncertainty import uncertainty


@pytest.fixture
def my_list():
    return list(range(10))


def test_uncertainty_list(my_list):
    u = uncertainty(my_list)
    assert isinstance(u, float)


def test_uncertainty_arr(my_list):
    my_arr = np.array(my_list)
    u = uncertainty(my_arr)
    assert isinstance(u, float)


def test_uncertainty_series(my_list):
    my_series = pd.Series(my_list)
    u = uncertainty(my_series)
    assert isinstance(u, float)
