import numpy as np
import pandas as pd
from typing import Union


def get_bin(
        df: pd.DataFrame,
        look: Union[int, float],
        depression: Union[int, float],
        bin_size: tuple[int, int] = (1, 5)
):
    assert 'Depression' in df.columns and 'Look' in df.columns, 'Data must have Look and Depression columns'

    # Filter by depression
    depr_width = bin_size[1]
    d0 = depression - depr_width / 2
    d1 = depression + depr_width / 2
    depr_mask = np.logical_and(df.Depression >= d0, df.Depression < d1)

    # Filter by look
    look_width = bin_size[0]
    l0 = look - look_width / 2
    l1 = look + look_width / 2
    if l0 < 0:
        l0 = 360 + l0
        logical_op = np.logical_or
    else:
        logical_op = np.logical_and
    look_mask = logical_op(df.Look >= l0, df.Look < l1)

    bin_mask = np.logical_and(depr_mask, look_mask)
    return df[bin_mask]
