import numpy as np
import pandas as pd

from lodat import Configuration
from lodat.data import DataObject
from lodat.stats import fences, uncertainty


class Algo(Configuration):
    def __init__(self, data_object_1: DataObject, data_object_2: DataObject):
        super(Algo, self).__init__()
        self.do1 = data_object_1
        self.do2 = data_object_2

    def analyze(self, frequency: float, polarization: str, bootstrap: bool = False):
        # Information from the config.ini
        look_centers = np.arange(
            start=int(self.config['LOOK']['min']),
            stop=int(self.config['LOOK']['max']),
            step=int(self.config['LOOK']['step'])
        )
        depr_centers = np.array(list(map(float, self.config['DEPRESSION']['center'].split(','))))

        # Step through each look
        df = pd.DataFrame()
        for depr in depr_centers:
            for look in look_centers:
                # Get hit data
                test_data = self.do1.slice_data(frequency, polarization, look, depr)
                base_data = self.do2.slice_data(frequency, polarization, look, depr)

                # Remove outliers
                test_fences = fences(test_data.RCS.values, float(self.config['ALGORITHM']['coverage_factor']))
                test_mask = np.logical_or(test_data.RCS < test_fences[0], test_data.RCS > test_fences[1])
                test_data = test_data[~test_mask]

                base_fences = fences(base_data.RCS.values, float(self.config['ALGORITHM']['coverage_factor']))
                base_mask = np.logical_or(base_data.RCS < base_fences[0], base_data.RCS > base_fences[1])
                base_data = base_data[~base_mask]

                # Bootstrap data
                if bootstrap:
                    num_iters = int(self.config['ALGORITHM']['bootstrap_iterations'])
                    test_rcs = np.random.choice(test_data.RCS, (len(test_data.RCS), num_iters), replace=True)
                    base_rcs = np.random.choice(base_data.RCS, (len(base_data.RCS), num_iters), replace=True)
                else:
                    test_rcs = test_data.RCS.values
                    base_rcs = base_data.RCS.values

                # Geometric mean
                test_gmn = np.mean(test_rcs)
                base_gmn = np.mean(base_rcs)

                # Uncertainty
                test_u = uncertainty(test_rcs, float(self.config['ALGORITHM']['significance_level']))
                base_u = uncertainty(base_rcs, float(self.config['ALGORITHM']['significance_level']))

                # Intervals
                test_interval = (test_gmn - test_u, test_gmn + test_u)
                base_interval = (base_gmn - base_u, base_gmn + base_u)

                # Statistically significant differences
                growth = min(test_interval) - max(base_interval)

                # Store the data
                s = pd.Series(
                    data=dict(
                        Look=look,
                        Depression=depr,
                        TestMean=test_gmn,
                        TestInterval=test_interval,
                        TestCount=len(test_rcs),
                        BaseMean=base_gmn,
                        BaseInterval=base_interval,
                        BaseCount=len(base_rcs),
                        Growth=growth
                    )
                )
                df = df.append(s, ignore_index=True)
        df.set_index(['Depression', 'Look'], inplace=True, drop=True)
        return df
