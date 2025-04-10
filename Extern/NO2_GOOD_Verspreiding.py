import pandas as pd
import matplotlib.pyplot as plt

PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')

good_no2_df = PlaceComplete_DF[(PlaceComplete_DF['no2 aqi value'] >= 0) & (PlaceComplete_DF['no2 aqi value'] <= 50)]

no2_counts = good_no2_df.groupby('no2 aqi value')['country'].nunique().reset_index(name='Country Count')

plt.figure(figsize=(12, 6))
plt.bar(no2_counts['no2 aqi value'], no2_counts['Country Count'], color='#1DE616')

plt.title('Aantal AQI-Waardes binnenin de Stikstofdioxide GOOD-Categorie (0-50)', fontsize=14)
plt.xlabel('NO2 AQI-Waarde', fontsize=12)
plt.ylabel('Aantal Landen', fontsize=12)

plt.grid(True)
plt.show()