import os
import itertools
import numpy as np
import pandas as pd
from pathos.pools import ProcessPool

from lodat.utils import get_bin


class FastDataObject:

    is_bin_data = False
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

        raw_data = self.raw_data.copy()

        self.frequencies = list(map(lambda x: f"{float(x):.1f}", self.raw_data.Frequency.unique().tolist()))
        self.polarizations = self.raw_data.Polarization.unique().tolist()

        vectors = list(itertools.product(self.frequencies, self.polarizations))

        def task(raw_data, vector):
            freq, pol = vector
            vector_mask = np.logical_and(raw_data.Frequency == float(freq), raw_data.Polarization == pol)
            df = raw_data[vector_mask]
            setattr(df, 'frequency', freq)
            setattr(df, 'polarization', pol)
            return df

        with ProcessPool(ncpus=os.cpu_count()-1) as pool:
            results = pool.uimap(task, itertools.repeat(raw_data), vectors)

        dct = {f: {p: pd.DataFrame() for p in self.polarizations} for f in self.frequencies}
        for df in list(results):
            dct[f"{df.Frequency.iloc[0]:.1f}"][df.Polarization.iloc[0]] = df

        return dct

    def get_bin_data(self, frequency: float, polarization: str, depression: float, bin_size=(1, 5)) -> pd.DataFrame:

        freq = f"{float(frequency):.1f}"
        pol = polarization.upper()
        vector = self.data[freq][pol]

        bin_data = dict()
        for look in np.arange(0, 360, bin_size[0]):
            bin_ = get_bin(vector, look, depression, bin_size)
            bin_data[look] = bin_.mean()
        return pd.DataFrame(bin_data).T
