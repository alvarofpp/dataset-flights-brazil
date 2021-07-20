# Flights in Brazil
This dataset have the flights in Brazil registered by ANAC (Agência Nacional de Aviação Civil - National Civil Aviation Agency).

- Source: [Dados Estatísticos](https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos).

## Scripts
- `extract.py` - Download all CSV files and puts them in the `data` folder.
- `transform.py` - Merge all files downloaded, rename the columns and create a final file (`anac.csv`).

## Generate
In your environment:

```shell
pip install -r requirements.txt

python3 extract.py

python3 transform.py
```

At the end you will have a file called `anac.csv` inside the `data` folder.

## Download
if you don't want to generate the final file, you can get the [`data/anac.zip`](data/anac.zip) file in this repository.

## Contributing
Contributions are more than welcome. Fork, improve and make a pull request. For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/dataset-flights-brazil/issues).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.