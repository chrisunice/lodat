import lodat as lo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def smooth(dot: lo.DataObject, window: int, method: str = 'percentile', **kwargs) -> lo.DataObject:
    """
    :param dot:
    :param window:
    :param method:
        - percentile: 0 to 100
        - amean: arithmetic mean; average in linear space
        - gmean: geometric mean; average in log space
    :return:
    """
    # Step through every set of bin data
    for freq in dot.frequencies:
        for pol in dot.polarizations:
            tmp = pd.DataFrame()
            for depr in dot.depressions:

                # Get bin data
                df = dot.get_bin_data(float(freq), pol, depr, bin_size=(dot.look_width, dot.bin_width))

                # Pad RCS data in preparation for smoothing
                rcs = df.RCS
                pad = np.ceil(window/2).astype(int)
                pad_left = rcs[-pad:]
                pad_right = rcs[:pad]
                padded_rcs = pd.concat((pad_left, rcs, pad_right))

                # Apply a smoothing function
                roll_kwargs = dict(window=window, min_periods=None, center=True, closed='both')
                if method == 'percentile':
                    smoothed_rcs = padded_rcs.rolling(**roll_kwargs).quantile(
                        quantile=kwargs['percentile']/100.0,
                        interpolation='linear'
                    )
                elif method == 'amean':
                    smoothed_rcs = padded_rcs.apply(lo.utils.tolinear).rolling(**roll_kwargs).mean()
                elif method == 'gmean':
                    smoothed_rcs = padded_rcs.rolling(**roll_kwargs).mean()
                else:
                    raise ValueError(f'Smoothing method of {method} is not supported')

                # Remove the padding
                smoothed_rcs = smoothed_rcs.iloc[pad:smoothed_rcs.size-pad]

                # Store in dataframe
                df.RCS = smoothed_rcs
                tmp = pd.concat((tmp, df))
            dot.data[freq][pol] = tmp
    return dot


if __name__ == '__main__':

    # Set up
    path_to_data = r"C:\LODAT\test_assets\test_data.csv"
    dot = lo.DataObject(path_to_data)
    dot.depressions = [-7.5, +2.5]
    dot.look_width = 1
    dot.bin_width = 5

    # Plot the difference
    freq, pol, depr = 8000, 'VV', +2.5
    fig, (ax0, ax1) = plt.subplots(ncols=2)

    # original
    df0 = dot.get_bin_data(freq, pol, depr)
    ax0.plot(df0.index, df0.RCS, c='r', label='Original Data')

    # smoothed
    dot = smooth(dot, window=11, percentile=70)
    df1 = dot.get_bin_data(freq, pol, depr)
    ax1.plot(df1.index, df1.RCS, c='b', label='Smoothed Data')
