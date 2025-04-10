import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

group1_regions = ['Asia Pacific', 'Middle East']
group2_regions = ['Europe', 'Africa', 'North America', 'Central and South America', 'Russia & Caspian']

group1_df = PlaceComplete_DF[
    (PlaceComplete_DF['region_x'].isin(group1_regions)) &
    (PlaceComplete_DF['ozone aqi category'] != 'Good') &
    (PlaceComplete_DF['pm2.5 aqi category'] != 'Good')
]

group2_df = PlaceComplete_DF[
    (PlaceComplete_DF['region_x'].isin(group2_regions)) &
    (PlaceComplete_DF['ozone aqi category'] != 'Good') &
    (PlaceComplete_DF['pm2.5 aqi category'] != 'Good')
]

plt.figure(figsize=(12, 8))

sns.regplot(
    x='pm2.5 aqi value', y='ozone aqi value', data=group1_df,
    scatter_kws={'s': 100, 'color': 'orange', 'label': 'Asia Pacific & Middle East', 'edgecolor': 'black'},
    line_kws={'color': 'orange'}
)

sns.regplot(
    x='pm2.5 aqi value', y='ozone aqi value', data=group2_df,
    scatter_kws={'s': 100, 'color': 'blue', 'label': 'Other Regions', 'edgecolor': 'black'},
    line_kws={'color': 'blue'}
)

plt.legend(fontsize=12, loc='upper left')

plt.title('Linear Regression of PM2.5 AQI Values and Ozone AQI Values by Region Groups', fontsize=16)
plt.xlabel('PM2.5 AQI Value', fontsize=14)
plt.ylabel('Ozone AQI Value', fontsize=14)

plt.tight_layout()

plt.show()
