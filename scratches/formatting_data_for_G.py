import pandas as pd


if __name__ == '__main__':

    # Read the CSV data
    path_to_data = r"C:\LODAT\test_assets\Gdata.xlsx"
    xlsx = pd.ExcelFile(path_to_data, engine='openpyxl')

    # Iterate through each sheet
    data = pd.DataFrame()
    for sheet in xlsx.sheet_names:
        # Get vector info
        freq, pol = sheet.split()

        # Read the data
        raw = pd.read_excel(xlsx, sheet_name=sheet, index_col=0, header=0)

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
