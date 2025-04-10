import pandas as pd
import matplotlib.pyplot as plt

pastels = ['#EF476F', '#F78C6B', '#FFD166', '#06D6A0', '#118AB2', '#073B4C']

category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

PlaceComplete_DF['co aqi category'] = pd.Categorical(
    PlaceComplete_DF['co aqi category'], 
    categories=category_order, 
    ordered=True
)

grouped_data = PlaceComplete_DF.groupby(['region', 'co aqi category'], observed=False).size().unstack(fill_value=0)

ax = grouped_data.plot(kind='bar', stacked=True, figsize=(12, 6), color=pastels)

totals = grouped_data.sum(axis=1)
for i, total in enumerate(totals):
    x = i
    ax.text(x, total + 0.5, int(total), ha='center', va='bottom')

plt.title('Stacked Bar Plot over CO AQI Categorie per Regio')
plt.xlabel('Regio')
plt.ylabel('Hoeveelheid Steden')
plt.xticks(rotation=45)
plt.legend(title='CO AQI Categorie', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
