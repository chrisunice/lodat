from functools import cached_property
import os
import itertools
import numpy as np
import dask.dataframe as dd
import pandas as pd

from lodat.utils import get_bin


class DaskDataObject:

    def __init__(self, path_to_file):
        """
        This is a shell of the full DataObject class at work. It will only support CSV files.

        :param path_to_file: full file path to a CSV
        """
        # Placeholder attributes
        self.frequencies = None
        self.polarizations = None

        # User inputs
        self.path_to_file = path_to_file

        # Build delayed components
        self._raw_data = self._get_raw_data()
        # self._data = self._get_data()

    @cached_property
    def raw_data(self) -> pd.DataFrame:
        return self._raw_data.compute()

    @cached_property
    def data(self) -> dict:
        # data_dict = dict()
        # for f, dct in self._data.items():
        #     data_dict[f] = dict()
        #     for p, dd_df in dct.items():
        #         data_dict[f][p] = dd_df.compute()
        return {f: {p: dd_df.compute() for p, dd_df in dct.items()} for f, dct in self._data.items()}

    def _get_raw_data(self) -> dd.DataFrame:
        dask_df = dd.read_csv(self.path_to_file)
        dask_df = dask_df.set_index(dask_df.columns[0], sorted=True, drop=True)
        dask_df.index = dask_df.index.rename(None)
        return dask_df

    def _get_data(self) -> dict:
        _freqs = self._raw_data.Frequency.unique().apply(lambda x: f"{float(x):.1f}", meta=('Frequency', 'object'))
        _pols = self._raw_data.Polarization.unique()

        dask_dict = dict()
        for f in _freqs:
            dask_dict[f] = dict()
            for p in _pols:
                vector_mask = (self._raw_data.Frequency == float(f)) & (self._raw_data.Polarization == p)
                dask_dict[f][p] = self._raw_data.mask(vector_mask)
        return dask_dict

    def get_bin_data(self, frequency: float, polarization: str, depression: float, bin_size=(1, 5)) -> dd.DataFrame:

        freq = f"{float(frequency):.1f}"
        pol = polarization.upper()
        vector = self.data[freq][pol]

        bin_data = dict()
        for look in np.arange(0, 360, bin_size[0]):
            bin_ = get_bin(vector, look, depression, bin_size)
            bin_data[look] = bin_.mean()
        return dd.DataFrame(bin_data).T
