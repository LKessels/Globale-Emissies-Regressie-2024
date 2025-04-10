import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filtered_df = PlaceComplete_DF[
    ((PlaceComplete_DF['region'] == 'Asia Pacific') | (PlaceComplete_DF['region'] == 'Middle East')) & 
    (PlaceComplete_DF['ozone aqi category'] != 'Good') & 
    (PlaceComplete_DF['pm2.5 aqi category'] != 'Good')
]

filtered_df = filtered_df[['pm2.5 aqi value', 'ozone aqi value']]

filtered_df = filtered_df.dropna()

plt.figure(figsize=(10, 6))
sns.regplot(x='pm2.5 aqi value', y='ozone aqi value', data=filtered_df, scatter_kws={'s': 100, 'color': 'blue', 'edgecolor': 'black'}, line_kws={'color': 'red'})

plt.title('Linear Regression tussen PM2.5 AQI-Waardes en Ozone AQI-Waardes', fontsize=14)
plt.xlabel('PM2.5 AQI-Waarde', fontsize=12)
plt.ylabel('Ozone AQI-Waarde', fontsize=12)

plt.tight_layout()
plt.show()
