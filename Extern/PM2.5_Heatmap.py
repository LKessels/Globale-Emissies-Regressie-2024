import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Region': ['Africa', 'Asia Pacific', 'Central and South America', 'Europe', 'Middle East', 'North America', 'Russia & Caspian'],
    'Good': [36.97, 22.55, 64.24, 56.31, 1.37, 34.42, 75.24],
    'Moderate': [42.80, 32.38, 27.84, 41.71, 34.25, 55.21, 19.93],
    'Unhealthy for Sensitive Groups': [9.71, 13.22, 4.56, 1.82, 26.03, 6.82, 3.36],
    'Unhealthy': [8.63, 26.45, 2.92, 0.17, 38.36, 2.90, 1.26],
    'Very Unhealthy': [1.57, 2.99, 0.40, 0.00, 0.00, 0.47, 0.14],
    'Hazardous': [0.32, 2.41, 0.04, 0.00, 0.00, 0.17, 0.07]
}

df = pd.DataFrame(data)
df.set_index('Region', inplace=True)

plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.5, cbar_kws={'label': 'Percentage'})

plt.title('PM2.5 AQI-Categorisatie Distributie per Regio')
plt.xlabel('PM2.5 AQI-Categorisatie')
plt.ylabel('Regio')

plt.show()
