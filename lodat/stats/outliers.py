import numpy as np
import pandas as pd
from typing import Union


def fences(array: Union[list, np.ndarray, pd.Series], coverage_factor: float = 1.5) -> tuple[float, float]:
    """
    Using the interquartile range method to provide lower and upper fences for outlier removal

    :param array: an iterable data object
    :param coverage_factor: typically denoted as `k`; it is a multiple of the IQR
    :return: the lower and upper fences, respectively
    """
    arr = np.array(array)
    assert arr.ndim == 1, "Array should be 1-D"

    q1 = np.quantile(arr, q=0.25)
    q3 = np.quantile(arr, q=0.75)
    iqr = q3 - q1

    lower_fence = q1 - coverage_factor * iqr
    upper_fence = q3 + coverage_factor * iqr
    return lower_fence, upper_fence
