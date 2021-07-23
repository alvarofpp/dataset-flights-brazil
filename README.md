# Flights in Brazil
This repository have datasets with all flights in Brazil registered by ANAC (Agência Nacional de Aviação Civil - National Civil Aviation Agency), all airports involved in these flights and a undirected graph with the number of flights between two airports.

- Sources:
  - [Flights in Brazil by ANAC](https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos).
  - [List of public aerodromes by ANAC](https://www.anac.gov.br/acesso-a-informacao/dados-abertos/areas-de-atuacao/aerodromos/lista-de-aerodromos-publicos-v2).
  - [Airport Codes by DataHub.io](https://datahub.io/core/airport-codes) (note: the latitude and longitude columns have their values swapped).

After merging the datasets, the [geocoder](https://github.com/DenisCarriere/geocoder) package was used to fill in the empty values.

## Datasets
You can find the datasets in `data/`.

### [`anac.zip`](data/anac.zip)
All flights in Brazil by ANAC. ANAC does not provide the data dictionary.

### [`airports.csv`](data/airports.csv)
All airports on ANAC flight records.

| Column | Type | Description | Example |
| --- | --- | --- | --- |
| code | `string` | [ICAO airport code](https://en.wikipedia.org/wiki/ICAO_airport_code) | `"SNBG"` |
| name | `string` | Airport name. | `"BAIXO GUANDU"` |
| state | `string` | State where the airport is located. | `"ES"` |
| region | `string` | Region where the airport is located. | `"SUDESTE"` |
| country | `string` | Country where the airport is located. | `"BRASIL"` |
| continent | `string` | Continent where the airport is located. | `"AMÉRICA DO SUL"` |
| lat_geo_point | `double` | Latitude of the airport reference point. | `-19.498889` |
| lon_geo_point | `double` | Longitude of the airport reference point. | `-41.041944` |

### [`air_traffic.graphml`](data/air_traffic.graphml)
It's an undirected graph.

#### Node attributes
The id of each node is the ICAO airport code.

| Column | Type | Description | Example |
| --- | --- | --- | --- |
| name | `string` | Airport name. | `"GUARULHOS"` |
| country | `string` | Country where the airport is located. | `"BRASIL"` |
| latitude | `double` | Latitude of the airport reference point. | `-23.435556` |
| longitude | `double` | Longitude of the airport reference point. | `-46.473056` |

#### Edge attributes
| Column | Type | Description | Example |
| --- | --- | --- | --- |
| flight_count | `int` | Number of flights carried out between these airports. | `147` |

## Scripts
- `extract.py` - Download all CSV files and puts them in the `data/extract` folder.
- `transform_to_anac_csv.py` - Merges all files downloaded from ANAC, rename the columns and create `anac.csv`.
- `transform_to_airports_csv.py` - Creates a dataset with all airports (`airports.csv`).
- `transform_to_graphml.py` - Creates an undirected graph (`air_traffic.graphml`).

## Generate
In your environment:

```shell
# Install requirements for scripts
pip install -r requirements.txt

# Download csv files from sources
python3 extract.py

# Transform to final files
python3 transform_to_anac_csv.py
python3 transform_to_airports_csv.py
python3 transform_to_graphml.py
```

## Contributing
Contributions are more than welcome. Fork, improve and make a pull request. For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/dataset-flights-brazil/issues).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
