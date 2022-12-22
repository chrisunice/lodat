import numpy as np
from typing import Union
from .tolinear import tolinear


_types = Union[int, float, np.ndarray]


def detection_range(delta: _types) -> _types:
    """
    Calculates the percent change in detection range
    :param delta: in dB
    :return: change in detection range as a percentage
    """
    rcs_ratio = tolinear(delta)
    dr = rcs_ratio**(1/4) - 1
    dr_percent = dr * 100
    return np.round(dr_percent, 0)
