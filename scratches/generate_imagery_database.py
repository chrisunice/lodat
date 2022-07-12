import os
import glob
import random
import sqlite3
import datetime
import numpy as np
import pandas as pd


def platform_gen():
    options = ['F22', 'F18', 'F35', 'F16', 'F15']
    yield random.choice(options)


def tail_gen():
    options = list(map(lambda x: f"AV{x}", range(5)))
    yield random.choice(options)


def umi_gen():
    options = list(map(lambda x: f"22{np.random.randint(100, 365)}", range(5)))
    yield random.choice(options)


def date_gen():
    options = []
    for i in range(5):
        month = np.random.randint(1, 12)
        day = np.random.randint(1, 28)
        date = datetime.datetime(2022, month, day).strftime('%Y-%m-%d')
        options.append(date)
    yield random.choice(options)


def band_gen():
    options = ['C', 'X', 'S', 'L', 'W']
    yield random.choice(options)


def pol_gen():
    options = ['VV', 'HH']
    yield random.choice(options)


def look_gen():
    yield np.random.randint(0, 360)


def depr_gen():
    yield np.round(np.random.rand()*10, 1)


def source_gen():
    options = ['P1', 'A1']
    yield random.choice(options)


def author_gen():
    options = ['Bob', 'Tom', 'John', 'Frank', 'Sam']
    yield random.choice(options)


def auto_gen():
    options = [0, 1]
    yield random.choice(options)


if __name__ == '__main__':

    # Create the database
    imagery_database_path = r"C:/LODAT/test_assets/imagery.sqlite"
    conn = sqlite3.connect(imagery_database_path)

    columns = [
        'Platform',
        'Tail',
        'UMI',
        'Date',
        'Band',
        'Polarization',
        'Look',
        'Depression',
        'Source',
        'Author',
        'Autoprocessed',
        'ImagePath'
    ]
    dct = {}
    for j, path in enumerate(glob.glob(f"{os.path.dirname(imagery_database_path)}\\images\\*.png")):
        dct[j] = [
            next(platform_gen()),
            next(tail_gen()),
            next(umi_gen()),
            next(date_gen()),
            next(band_gen()),
            next(pol_gen()),
            next(look_gen()),
            next(depr_gen()),
            next(source_gen()),
            next(author_gen()),
            next(auto_gen()),
            path
        ]
    data = pd.DataFrame(data=dct).T
    data.columns = columns
    conn.execute("DROP TABLE IF EXISTS data")
    data.to_sql(name='data', con=conn)
