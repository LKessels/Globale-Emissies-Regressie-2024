import pandas as pd
import matplotlib.pyplot as plt

category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

PlaceComplete_DF['pm2.5 aqi category'] = pd.Categorical(
    PlaceComplete_DF['pm2.5 aqi category'], 
    categories=category_order, 
    ordered=True
)

grouped_data = PlaceComplete_DF.groupby(['region', 'pm2.5 aqi category'], observed=False).size().unstack(fill_value=0)

totals_including_good = grouped_data.sum(axis=1)
totals_excluding_good = grouped_data.drop(columns="Good", errors='ignore').sum(axis=1)

percentage_not_good = (totals_excluding_good / totals_including_good * 100).round(2)

table_data = pd.DataFrame({
    'Regio': grouped_data.index,
    'Totaal met Good': totals_including_good,
    'Totaal zonder Good': totals_excluding_good,
    '% van Totaal': percentage_not_good
}).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(8, len(table_data) * 0.5))
ax.axis('off')

table = plt.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0, 1, 2, 3])

plt.title('Ozone AQI voorkoming per Regio', fontsize=12, pad=20)
plt.show()
