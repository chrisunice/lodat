import random
import numpy as np
import pandas as pd


if __name__ == '__main__':

    # Radar transmit parameters
    freq0 = 300
    freq1 = 1000
    num_freqs = 1024
    frequencies = np.arange(freq0, freq1, (freq1-freq0)/num_freqs)
    polarizations = ['HH', 'VV']
    depressions = [2.5, -7.5]

    # Aircraft collection parameters
    hits_per_bin = 10
    data = pd.DataFrame()
    for depr in depressions:
        for freq in frequencies:
            for pol in polarizations:

                # Fake look angles
                look_base = np.linspace(0, 360, num=hits_per_bin*360, endpoint=False)
                look_noise = np.random.randn(hits_per_bin*360) * 0.1
                look = look_base + look_noise

                # Fake depression angles
                depr_noise = np.random.randn(len(look)) * 0.5
                depr_base = np.ones(len(look)) * depr
                depression = depr_base + depr_noise

                # Fake twist angles
                twist = np.random.randn(len(look)) * 5

                # Fake RCS data for a 1 meter diameter sphere
                rcs_base = np.pi*0.5**2
                rcs = np.random.normal(rcs_base, 5, len(look))

                # Add random growth
                num_growths = 1000
                rand_idx = random.sample(range(len(rcs)), num_growths)
                growths = np.random.randint(0, 100, size=(num_growths,))
                rcs[rand_idx] = rcs[rand_idx] + growths

                tmp = pd.DataFrame(
                    data=dict(
                        Look=look,
                        Depression=depression,
                        Twist=twist,
                        Frequency=freq,
                        Polarization=pol,
                        RCS=rcs
                    )
                )
                data = pd.concat((data, tmp))

    output_path = f"C:\\LODAT\\imagery_data.csv"
    data.to_csv(output_path)
