import pandas as pd
import matplotlib.pyplot as plt

PlaceComplete_DF = pd.read_csv('MergedDatasetsDF.csv', delimiter=';')

type_counts = PlaceComplete_DF['type'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']

plt.figure(figsize=(10, 6))
bars = plt.bar(type_counts['Type'], type_counts['Count'], color='skyblue')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom', fontsize=10)

plt.title('Hoeveelheid Voorkomende Emissietypes')
plt.xlabel('Emissietype')
plt.ylabel('Aantal Voorkomingen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()