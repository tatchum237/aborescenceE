import pandas as pd


def load_data(url = 'data/house.csv'):
    return pd.read_csv(url)

def clean_data(data):
    # Supprimer les lignes dupliquées
    data = data.drop_duplicates()
    # Gérer les valeurs manquantes en les remplaçant
    for column in data.columns:
        data[column].fillna(data[column].mean, inplace=True)
    return data

def delete_data(data):
    # Supprimer les lignes dupliquées
    data = data.drop_duplicates()

    return data

def feature_enineer(data):
    data['city'] = data['city'].apply(lambda x: call_name_pays(x))
    data['country'] = data['country'].apply(lambda x: call_name(x))

    return data


def call_name(dat):
    pays = dat[28:50]
    return pays.split('\'')[0]


def call_name_pays(dat):
  pays = dat[10:25]
  return pays.split('\'')[0]


def show_stat(data):
    pass
   
   

#if __name__=="__main__":
# Charger vos données

data = load_data()

# Appeler les fonctions en série
data = clean_data(data)

data = delete_data(data)

data = feature_enineer(data)


show_stat(data)







