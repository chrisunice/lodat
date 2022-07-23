import numpy as np
import pandas as pd
import lodat as lo


def test_standard_error():
    arr = np.arange(10)
    se = lo.stats.standarderror(arr)
    assert isinstance(se, float)


def test_list_type():
    lst = list(np.arange(10))
    se = lo.stats.standarderror(lst)
    assert isinstance(se, float)


def test_series_type():
    s = pd.Series(np.arange(10))
    se = lo.stats.standarderror(s)
    assert isinstance(se, float)
