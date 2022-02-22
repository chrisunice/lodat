import numpy as np
import pandas as pd
from typing import Union
from sklearn.utils import resample


def bootstrap(array: Union[list, np.ndarray, pd.Series], num_iterations: int) -> np.ndarray:
    arr = np.array(array)
    assert arr.ndim == 1, "Array should be 1-D"

    # TODO this should be improved with multiprocessing or cython
    boot_samples = np.random.choice(arr, (len(arr), num_iterations), replace=True)

    means = map(
        lambda x: np.mean(resample(arr, replace=True, n_samples=len(arr))),
        range(num_iterations)
    )
    return np.array(list(means))


