import time
import timeit
import lodat as lo
import numpy as np
from pathos import pools
from itertools import repeat
import multiprocessing as mp


def benchmark(dot: lo.DataObject, retval: dict):
    for f in dot.frequencies:
        for p in dot.polarizations:
            mask = np.logical_and(dot.raw_data.Frequency == float(f), dot.raw_data.Polarization == p)
            tmp = dot.raw_data[mask]
            tmp.reset_index(inplace=True, drop=True)
            retval[f][p] = tmp
    return retval


def improved_filtering(dot: lo.DataObject, retval: dict):
    for f in dot.frequencies:
        for p in dot.polarizations:
            mask = (dot.raw_data.Frequency.values == float(f)) & (dot.raw_data.Polarization.values == p)
            tmp = dot.raw_data[mask]
            tmp.reset_index(inplace=True, drop=True)
            retval[f][p] = tmp
    return retval


def using_map(dot: lo.DataObject, retval: dict):
    vectors = [(f, p) for p in dot.polarizations for f in dot.frequencies]

    def func(vector):
        f, p, = vector
        # mask = np.logical_and(dot.raw_data.Frequency == float(f), dot.raw_data.Polarization == p)
        mask = (dot.raw_data.Frequency.values == float(f)) & (dot.raw_data.Polarization.values == p)
        tmp = dot.raw_data[mask]
        tmp.reset_index(inplace=True, drop=True)
        retval[f][p] = tmp
        return None

    _ = list(map(func, vectors))
    return retval


def task(vector, shared_namespace, shared_dict):
    # Unpack arguments
    f, p, = vector
    df = shared_namespace.df

    # Slice dataframe
    mask = (df.Frequency.values == float(f)) & (df.Polarization.values == p)
    tmp = df[mask]
    tmp.reset_index(inplace=True, drop=True)
    shared_dict[f"{f}-{p}"] = tmp

    return None


if __name__ == '__main__':

    path_to_data = r"C:\LODAT\test_assets\large_data.csv"
    my_dot = lo.DataObject(path_to_data)

    # Pre-allocating object to store data
    data = {f: {p: None for p in my_dot.polarizations} for f in my_dot.frequencies}

    # TIMING
    iterations = 1

    # Benchmark (nested for loops)
    t_bench = timeit.timeit(lambda: benchmark(my_dot, data), number=iterations)
    print(f'\nBenchmark: {t_bench/iterations:.3f} seconds')

    # Better filter (nested for loops)
    t_filter = timeit.timeit(lambda: improved_filtering(my_dot, data), number=iterations)
    print(f'\nBetter filtering: {t_filter / iterations:.3f} seconds')

    # Using map
    t_map = timeit.timeit(lambda: using_map(my_dot, data), number=iterations)
    print(f'\nUsing map: {t_map/iterations:.3f} seconds')

    # Using parallel starmap
    t0 = time.time()
    vectors = [(f, p) for p in my_dot.polarizations for f in my_dot.frequencies]
    chunk_size = len(vectors)//mp.cpu_count()
    with mp.Manager() as mgr:
        namespace = mgr.Namespace()
        namespace.df = my_dot.raw_data
        d = mgr.dict()

        with mp.Pool() as pool:
            pool.starmap(task, zip(vectors, repeat(namespace), repeat(d)), chunksize=chunk_size)

        bin_data = {}
        for k, v in d.items():
            f, p = k.split('-')
            bin_data[f] = {}
            bin_data[f][p] = v
    t1 = time.time()
    print(f'\nUsing parallel starmap: {t1-t0:.3f} seconds')
