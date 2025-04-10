import pandas as pd
import matplotlib.pyplot as plt

PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')

good_co_df = PlaceComplete_DF[(PlaceComplete_DF['co aqi value'] >= 0) & (PlaceComplete_DF['co aqi value'] <= 50)]

co_counts = good_co_df.groupby('co aqi value')['country'].nunique().reset_index(name='Country Count')

plt.figure(figsize=(12, 6))
plt.bar(co_counts['co aqi value'], co_counts['Country Count'], color='#1DE616')

plt.title('Aantal AQI-Waardes binnenin de Koolstofmonoxide GOOD-Categorie (0-50)', fontsize=14)
plt.xlabel('CO AQI-Waarde', fontsize=12)
plt.ylabel('Aantal Landen', fontsize=12)

plt.grid(True)
plt.show()
