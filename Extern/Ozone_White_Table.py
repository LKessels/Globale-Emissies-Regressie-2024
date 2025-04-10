import pandas as pd
import matplotlib.pyplot as plt

category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

PlaceComplete_DF['ozone aqi category'] = pd.Categorical(
    PlaceComplete_DF['ozone aqi category'], 
    categories=category_order, 
    ordered=True
)

grouped_data = PlaceComplete_DF.groupby(['region', 'ozone aqi category'], observed=False).size().unstack(fill_value=0)

grouped_data_without_good = grouped_data.drop(columns="Good", errors='ignore')


table_data = grouped_data_without_good.sum(axis=1).reset_index()
table_data.columns = ['Regio', 'Total Aantal AQI-Waardes (GOOD weggelaten)']


fig, ax = plt.subplots(figsize=(6, len(table_data) * 0.5))
ax.axis('off')

table = plt.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0, 1])
plt.title('Total Aantal AQI-Waardes per Regio (GOOD weggelaten)', fontsize=12, pad=20)
plt.show()
