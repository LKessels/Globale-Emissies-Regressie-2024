import pandas as pd
import matplotlib.pyplot as plt

pastels = ['#FFFFFF', '#EBE404', '#EA8305', '#FC0000', '#893395', '#800000']

category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

PlaceComplete_DF['ozone aqi category'] = pd.Categorical(
    PlaceComplete_DF['ozone aqi category'], 
    categories=category_order, 
    ordered=True
)

grouped_data = PlaceComplete_DF.groupby(['region', 'ozone aqi category'], observed=False).size().unstack(fill_value=0)

grouped_data_without_good = grouped_data.drop(columns="Good", errors='ignore')

ax = grouped_data.plot(kind='bar', stacked=True, figsize=(12, 6), color=pastels, edgecolor='black')

plt.title('Ozone AQI Categorie per Regio')
plt.xlabel('Regio')
plt.ylabel('Hoeveelheid Steden')
plt.xticks(rotation=45)
plt.legend(title='Ozone AQI Categorie', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()