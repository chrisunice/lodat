import numpy as np
import pandas as pd
from scipy import stats
from typing import Union

from .standarderror import standarderror


def uncertainty(array: Union[list, np.ndarray, pd.Series], significance_level: float = 0.05) -> float:
    arr = np.array(array)

    # Standard error
    se = standarderror(arr)

    # Uncertainty
    t_value = stats.t.ppf(q=1 - (significance_level / 2), df=len(arr))

    return t_value * se
