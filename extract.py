import os.path
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

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

    file_response = requests.get(link)
    open(filename, 'wb').write(file_response.content)

# Public aerodromes (ANAC)
url = 'https://sistemas.anac.gov.br/dadosabertos/Aerodromos/Lista%20de%20aer%C3%B3dromos%20p%C3%BAblicos/AerodromosPublicos.csv'
file_response = requests.get(url)
open(path + 'public_aerodromes.csv', 'wb').write(file_response.content)

# Airport Codes (DataHub.io)
url = 'https://datahub.io/core/airport-codes/r/airport-codes.csv'
file_response = requests.get(url)
open(path + 'airport_codes.csv', 'wb').write(file_response.content)
