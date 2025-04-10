import pandas as pd
import matplotlib.pyplot as plt

pastels = ['#1DE616', '#EBE404', '#EA8305', '#FC0000', '#893395', '#800000']

category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

PlaceComplete_DF['pm2.5 aqi category'] = pd.Categorical(
    PlaceComplete_DF['pm2.5 aqi category'], 
    categories=category_order, 
    ordered=True
)

grouped_data = PlaceComplete_DF.groupby(['region', 'pm2.5 aqi category'], observed=False).size().unstack(fill_value=0)

ax = grouped_data.plot(kind='bar', stacked=True, figsize=(12, 6), color=pastels)

totals = grouped_data.sum(axis=1)
for i, total in enumerate(totals):
    x = i
    ax.text(x, total + 0.5, int(total), ha='center', va='bottom')

plt.title('PM2.5 AQI Categorie per Regio')
plt.xlabel('Regio')
plt.ylabel('Hoeveelheid Steden')
plt.xticks(rotation=45)
plt.legend(title='PM2.5 AQI Categorie', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
