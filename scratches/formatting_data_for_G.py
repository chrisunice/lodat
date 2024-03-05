import os
import glob
import pandas as pd


if __name__ == '__main__':

    # Read the CSV data
    csv_directory = r"C:\LODAT\test_assets\Gdata"

    # Iterate through each sheet
    data = pd.DataFrame()
    for csv_path in glob.glob(f"{csv_directory}\\*.csv"):
        # Get vector info
        fname = os.path.basename(csv_path)
        freq, pol = os.path.splitext(os.path.basename(fname))[0].split()

        # Read the data
        raw = pd.read_csv(csv_path, index_col=0, header=0)

        # Add a Look column based on the index
        raw = raw.reset_index(names='Depression')

        # Unpivot the data
        raw = raw.melt(id_vars=['Depression'], var_name='Look', value_name='RCS')

        # Add vector columns
        raw['Frequency'] = freq
        raw['Polarization'] = pol

        # Store the data
        data = pd.concat((data, raw))

    # Extract some meta data
    frequencies = data.Frequency.unique().tolist()
    polarizations = data.Frequency.unique().tolist()
    looks = data.Look.unique().tolist()
    depressions = data.Depression.unique().tolist()

    # Create FBIN
    # TODO take the code from work
