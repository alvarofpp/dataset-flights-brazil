import glob
import pandas as pd

files = glob.glob('data/extract/resumo_anual_*.csv')

# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(file, sep=';', encoding='ISO-8859-1') for file in files])

# Rename columns
columns_map = {
    'EMPRESA (SIGLA)': 'company_abbreviation',
    'EMPRESA (NOME)': 'company_name',
    'EMPRESA (NACIONALIDADE)': 'company_nationality',
    'ANO': 'year',
    'MÊS': 'month',
    'AEROPORTO DE ORIGEM (SIGLA)': 'origin_airport_abbreviation',
    'AEROPORTO DE ORIGEM (NOME)': 'origin_airport_name',
    'AEROPORTO DE ORIGEM (UF)': 'origin_airport_state',
    'AEROPORTO DE ORIGEM (REGIÃO)': 'origin_airport_region',
    'AEROPORTO DE ORIGEM (PAÍS)': 'origin_airport_country',
    'AEROPORTO DE ORIGEM (CONTINENTE)': 'origin_airport_continent',
    'AEROPORTO DE DESTINO (SIGLA)': 'destination_airport_abbreviation',
    'AEROPORTO DE DESTINO (NOME)': 'destination_airport_name',
    'AEROPORTO DE DESTINO (UF)': 'destination_airport_state',
    'AEROPORTO DE DESTINO (REGIÃO)': 'destination_airport_region',
    'AEROPORTO DE DESTINO (PAÍS)': 'destination_airport_country',
    'AEROPORTO DE DESTINO (CONTINENTE)': 'destination_airport_continent',
    'NATUREZA': 'nature',
    'GRUPO DE VOO': 'flight_group',
    'PASSAGEIROS PAGOS': 'paid_passenger',
    'PASSAGEIROS GRÁTIS': 'free_passenger',
    'CARGA PAGA (KG)': 'charge_paid_kg',
    'CARGA GRÁTIS (KG)': 'charge_free_kg',
    'CORREIO (KG)': 'mail_kg',
    'ASK': 'ask',
    'RPK': 'rpk',
    'ATK': 'atk',
    'RTK': 'rtk',
    'COMBUSTÍVEL (LITROS)': 'fuel_l',
    'DISTÂNCIA VOADA (KM)': 'distance_flown_km',
    'DECOLAGENS': 'takeoffs',
    'CARGA PAGA KM': 'charge_paid_km',
    'CARGA GRATIS KM': 'charge_free_km',
    'CORREIO KM': 'mail_km',
    'ASSENTOS': 'seats',
    'PAYLOAD': 'payload',
    'HORAS VOADAS': 'fly_hours',
    'BAGAGEM (KG)': 'baggage_kg',
}
combined_csv = combined_csv.rename(columns=columns_map)

# Export to csv
combined_csv.to_csv('data/anac.csv', index=False, encoding='utf-8')
