import timeit
if __name__ == '__main__':

    path_to_data = r"C:\LODAT\test_assets\large_data.csv"

    # Old dot
    from lodat.data import DataObject
    print(timeit.timeit(lambda: DataObject(path_to_data), number=1))

    # New dot
    from lodat.data.fast_data_object import FastDataObject
    print(timeit.timeit(lambda: DataObject(path_to_data), number=1))
