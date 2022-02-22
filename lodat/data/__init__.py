import numpy as np
import pandas as pd
from typing import Union


class DataObject:

    frequencies: list[str] = None
    polarizations: list[str] = None

    def __init__(self, path_to_file):
        """
        This is a shell of the full DataObject class at work. It will only support CSV files.

        :param path_to_file: full file path to a CSV
        """
        self.path_to_file = path_to_file
        self.raw_data = self._get_raw_data()
        self.data = self._get_data()

    def _get_raw_data(self):
        return pd.read_csv(self.path_to_file, index_col=0)

    def _get_data(self):

        self.frequencies = list(map(lambda x: f"{float(x):.1f}", self.raw_data.Frequency.unique().tolist()))
        self.polarizations = self.raw_data.Polarization.unique().tolist()

        data = dict()
        for freq in self.frequencies:
            data[freq] = dict()
            for pol in self.polarizations:
                vector_mask = np.logical_and(self.raw_data.Frequency == float(freq), self.raw_data.Polarization == pol)
                data[freq][pol] = self.raw_data[vector_mask]
        return data

    def slice_data(self, frequency: float, polarization: str, look: Union[int, float],
                   depression: Union[int, float], bin_size: tuple[int, int] = (1, 5)):
        # Handle parameters
        freq = f"{float(frequency):.1f}"
        pol = polarization.upper()

        vector = self.data[freq][pol]

        # Filter by depression
        depr_width = bin_size[1]
        d0 = depression - depr_width/2
        d1 = depression + depr_width/2
        depr_mask = np.logical_and(vector.Depression >= d0, vector.Depression < d1)

        # Filter by look
        look_width = bin_size[0]
        l0 = look - look_width/2
        l1 = look + look_width/2
        if l0 < 0:
            l0 = 360 + l0
            logical_op = np.logical_or
        else:
            logical_op = np.logical_and
        look_mask = logical_op(vector.Look >= l0, vector.Look < l1)

        bin_mask = np.logical_and(depr_mask, look_mask)
        return vector[bin_mask]
