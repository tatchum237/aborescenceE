import pandas as pd


def load_data(url = 'data/house.csv'):
    return pd.read_csv(url)

def clean_data(data):

    # Gérer les valeurs manquantes en les remplaçant
    for column in data.columns:
        data[column].fillna(data[column].mean, inplace=True)
    return data








