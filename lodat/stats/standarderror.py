import numpy as np
import pandas as pd
from typing import Union


def standarderror(array: Union[list, np.ndarray, pd.Series]) -> float:
    arr = np.array(array)

    if arr.ndim == 1:
        std_dev = np.std(arr, ddof=1)
    else:
        std_dev = np.std(arr, axis=0, ddof=1).mean()

    samples = len(arr)
    error = std_dev / np.sqrt(samples)
    return error
