import geocoder
import pandas as pd

path = 'data/extract/'

# ANAC dataset
anac_columns = [
    'origin_airport_abbreviation',
    'origin_airport_name',
    'origin_airport_state',
    'origin_airport_region',
    'origin_airport_country',
    'origin_airport_continent',
    'destination_airport_abbreviation',
    'destination_airport_name',
    'destination_airport_state',
    'destination_airport_region',
    'destination_airport_country',
    'destination_airport_continent',
]
df_anac = pd.read_csv('data/anac.csv', usecols=anac_columns)

# Get airports from ANAC
same_columns = {
    'origin_airport_abbreviation': 'code',
    'origin_airport_name': 'name',
    'origin_airport_state': 'state',
    'origin_airport_region': 'region',
    'origin_airport_country': 'country',
    'origin_airport_continent': 'continent',
    'destination_airport_abbreviation': 'code',
    'destination_airport_name': 'name',
    'destination_airport_state': 'state',
    'destination_airport_region': 'region',
    'destination_airport_country': 'country',
    'destination_airport_continent': 'continent',
}
origin_columns = [
    'origin_airport_abbreviation',
    'origin_airport_name',
    'origin_airport_state',
    'origin_airport_region',
    'origin_airport_country',
    'origin_airport_continent',
]
destination_columns = [
    'destination_airport_abbreviation',
    'destination_airport_name',
    'destination_airport_state',
    'destination_airport_region',
    'destination_airport_country',
    'destination_airport_continent',
]

df_origins = df_anac[origin_columns]
df_origins = df_origins.rename(columns=same_columns)

df_destinations = df_anac[destination_columns]
df_destinations = df_destinations.rename(columns=same_columns)

df_airports = pd.concat([df_origins, df_destinations])
df_airports = df_airports.drop_duplicates()

# Airfields dataset
airfields_columns = [
    'Código OACI',
    'LATGEOPOINT',
    'LONGEOPOINT',
]
df_airfields = pd.read_csv(path + 'public_aerodromes.csv',
                           sep=';',
                           usecols=airfields_columns,
                           skiprows=1,
                           encoding='ISO-8859-1')

# Rename columns
columns_map = {
    'CÓDIGO OACI': 'code',
    'LATGEOPOINT': 'lat_geo_point',
    'LONGEOPOINT': 'lon_geo_point',
}
df_airfields = df_airfields.rename(columns=columns_map)

# Others airports
others_airports_columns = [
    'ident',
    'coordinates',
]
df_others_airports = pd.read_csv(path + 'airport_codes.csv', usecols=others_airports_columns)

# Rename columns
columns_map = {
    'ident': 'code',
}
df_others_airports = df_others_airports.rename(columns=columns_map)
df_others_airports[['lon_geo_point', 'lat_geo_point']] = df_others_airports.coordinates.str.split(', ', expand=True, )
df_others_airports = df_others_airports.drop(columns=['coordinates'])

# Coordinates dataframe
df_coordinates = pd.concat([df_airfields, df_others_airports])

# Merge dataframe
df_merge = pd.merge(
    df_airports,
    df_coordinates,
    how='left',
    left_on='code',
    right_on='code')
df_merge = df_merge.dropna(how='all')
df_merge = df_merge.drop_duplicates('code')

# Find the others geolocations
columns = [
    'name',
    'state',
    'region',
    'country',
    'continent',
]
airports_to_find = []
for index, row in df_merge[df_merge.lat_geo_point.isnull()].iterrows():
    label = ''

    for column in columns:
        if type(row[column]) == str and row[column]:
            label += row[column] + ', '

    if not label:
        continue

    geo_result = geocoder.arcgis(label[:-2])
    df_merge.loc[df_merge.code == row['code'], 'lat_geo_point'] = geo_result.latlng[0]
    df_merge.loc[df_merge.code == row['code'], 'lon_geo_point'] = geo_result.latlng[1]

# Save result
df_merge.to_csv('data/airports.csv', index=False, encoding='utf-8')
