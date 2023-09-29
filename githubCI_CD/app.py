import pandas as pd


def load_data(url = 'data/house.csv'):
    return pd.read_csv(url)

def clean_data(data):

    # Gérer les valeurs manquantes en les remplaçant
    for column in data.columns:
        data[column].fillna(data[column].mean, inplace=True)
    return data

def delete_data(data):
    # Supprimer les lignes dupliquées
    data = data.drop_duplicates()
    data = data.drop(
        ['Unnamed: 0', 'rent_per_day', 'dimension', 'tv_liveroom', 'colocation', 'tv_all_bedroom', 'climatisation',
         'wifi', 'gym', 'hot_water', 'swimming_pool', 'cooker', 'freezer', 'is_booked.1', 'is_booked', 'fence',
         'elevator', 'pets_allowed', 'is_furnished', 'is_finished', 'events_allowed', 'suitable_for_children',
         'smooking_allowed', 'is_negociable', 'name', 'id', 'disponible', 'gcel', 'desciption', 'publish', 'ia',
         'water_m3_price', 'electricity_Kw_price', 'number_of_person_allowed', 'moyenne', 'nb_partageur',
         'nb_reserveur', 'user', 'sexe_colocataire', 'age_colocataire', 'religion_colocataire',
         'religion_colocataire.1', 'checkin_time', 'checkout_time', 'date_created', 'lien', 'partageurs', 'reserveurs'],
        axis=1)
    return data


def feature_enineer(data):
    data['city'] = data['city'].apply(lambda x: call_name_pays(x))
    data['country'] = data['country'].apply(lambda x: call_name(x))
    data['date_created'] = data['date_created'].apply(lambda x: x.split('/')[0])
    return data

def call_name(dat):
  pays = dat[28:50]
  return pays.split('\'')[0]


def call_name_pays(dat):
  pays = dat[10:25]
  return pays.split('\'')[0]


def show_stat(data):
    data[['renting_price', 'is_immeuble']].groupby(['is_immeuble'], as_index=False).mean().sort_values(
        by='renting_price', ascending=False)
    data[['renting_price', 'is_moderne']].groupby(['is_moderne'], as_index=False).mean().sort_values(by='renting_price',
                                                                                                     ascending=False)

    data[['city', 'renting_price', 'is_immeuble', 'category']].groupby(['city', 'is_immeuble', 'category'],
                                                                       as_index=False).sum().sort_values(
        by='renting_price', ascending=False)













