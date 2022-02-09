import numpy as np
import pandas as pd


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
