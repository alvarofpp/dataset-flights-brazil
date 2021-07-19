import os.path
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

# Request
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
    filename = 'data/' + link.split('/')[-1]
    if os.path.exists(filename):
        continue

    file_response = requests.get(link)
    open(filename, 'wb').write(file_response.content)
