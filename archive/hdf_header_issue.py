import h5py
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)


if __name__ == '__main__':

    # Read some data into a DataFrame
    data = pd.read_csv(r"C:\LODAT\test_assets\baseline_data.csv", index_col=0)

    # Convert the dataframe into records which is a list of row by row values
    records = data.to_records(index=False)

    # Need to change the Object types for 'S10' or something that HDF5 will accept
    # [('Look', 'f4'), ('Depression', 'f4'), ('Twist', 'f4'), ('Frequency', 'f4'), ('Polarization', 'S10'), ('RCS', 'f4')]
    current_dtypes = records.dtype.descr
    current_dtypes[-2] = ('Polarization', 'S10')
    arr = np.array(records, dtype=current_dtypes)

    # Open/Create an HDF5 file
    with h5py.File(r"C:\LODAT\test_assets\mpf.h5", 'w') as h5:
        h5.create_dataset('bin_data', data=arr)

    print('Done!')
