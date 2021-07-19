import glob
import pandas as pd

files = glob.glob('data/resumo_anual_*.csv')
# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(file, sep=';', encoding='ISO-8859-1') for file in files])

# Export to csv
combined_csv.to_csv("data/anac.csv", index=False, encoding='utf-8')
