import os.path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

path = 'data/extract/'

# Flights (ANAC)
url = 'https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get all links
tags_a = soup.find_all('a', {
    'target': '_self',
    'class': 'internal-link',
})
links = [tag_a['href'] for tag_a in tags_a if tag_a['href'].endswith('.csv')]

# Download all files
for link in tqdm(links):
    filename = path + link.split('/')[-1]
    if os.path.exists(filename):
        continue

    with requests.get(link) as file_response, open(filename, 'wb') as file_to_save:
        file_to_save.write(file_response.content)

# Public aerodromes (ANAC)
public_aerodromes_filepath = path + 'public_aerodromes.csv'
if not os.path.exists(public_aerodromes_filepath):
    url = 'https://sistemas.anac.gov.br/dadosabertos/Aerodromos/Aer%C3%B3dromos%20P%C3%BAblicos/Lista%20de%20aer%C3%B3dromos%20p%C3%BAblicos/AerodromosPublicos.csv'
    with requests.get(url) as file_response, \
            open(public_aerodromes_filepath, 'wb') as file_to_save:
        file_to_save.write(file_response.content)

# Airport Codes (DataHub.io)
airport_codes_filepath = path + 'airport_codes.csv'
if not os.path.exists(airport_codes_filepath):
    url = 'https://datahub.io/core/airport-codes/r/airport-codes.csv'
    with requests.get(url) as file_response, \
            open(airport_codes_filepath, 'wb') as file_to_save:
        file_to_save.write(file_response.content)
