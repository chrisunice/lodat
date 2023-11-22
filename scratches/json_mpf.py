import json
import random
import string

import h5py
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)


def generate_random_fname(length: int):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


if __name__ == '__main__':

    # file_name_options = [
    #     'A',
    #     'A, B',
    #     'C, D, F, G, D'
    # ]
    #
    # Read some data into a DataFrame
    # data = pd.read_csv(r"C:\LODAT\test_assets\baseline_data.csv", index_col=0)
    # data.reset_index(drop=True, inplace=True)
    #
    # json_object = data.head().to_dict(orient='list')
    #
    # json_fpath = r"C:\LODAT\test_assets\mpf.json"
    # with open(json_fpath, 'w') as json_file:
    #     json.dump(json_object, json_file)

    data = np.array([(1, 2.5, 'Hello'), (3, 4.0, 'World')],
                    dtype=[('int_col', 'i4'), ('float_col', 'f4'), ('str_col', 'S10')])

    # data['FileName'] = [np.random.choice(file_name_options) for _ in range(len(data))]

    # data_num = data.select_dtypes(exclude='object')
    # data_cat = data.select_dtypes(include='object')

    # Open/Create an HDF5 file
    with h5py.File(r"C:\LODAT\test_assets\mpf.h5", 'w') as h5:
        h5.create_dataset('bin_data', data=data)

    # Add dataframe
    # data.to_hdf(hdf_file_path, key='my_data', mode='w', format='table', data_columns=True)
    # ds = hdf_file.create_dataset('bin_data', np.random.randint(0, 10, size=(10, 10)), dtype='i8')

    # data.Polarization = data.Polarization.astype(str)

    # structured_data = data.to_records(index=False)

    # ds = hdf_file.create_dataset('bin_data2', data=structured_data)

    # ds.attrs['FileName'] = generate_random_fname(100)

    # Close HDF5 file
    # hdf_file.close()

    print('Done!')
