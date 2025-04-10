import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

energy_data = MergedDatasetsDF[MergedDatasetsDF['type'] == 'Energy'][['aqi value', 'aqi category']].copy()

bins = range(0, 361, 10)

plt.figure(figsize=(10, 6))

n, bins, patches = plt.hist(energy_data['aqi value'], bins=bins, edgecolor='black', alpha=0.7)

bin_colors = ['green'] * 5 + ['yellow'] * 5 + ['orange'] * 5 + ['red'] * 5 + ['purple'] * 10 + ['maroon'] * (len(bins) - 25)

for i in range(len(patches)):
    patches[i].set_facecolor(bin_colors[i])

plt.title('Distributie van AQI-Waardes voor het emissietype Energie', fontsize=14)
plt.xlabel('AQI-Waarde', fontsize=12)
plt.ylabel('Aantal Voorkomingen', fontsize=12)

legend_labels = ['Good (0-50)', 'Moderate (51-100)', 'Unhealthy for Sensitive Groups (101-150)', 
                 'Unhealthy (151-200)', 'Very Unhealthy (201-300)', 'Hazardous (301+)']

legend_patches = [
    mpatches.Patch(color='green', label='Good (0-50)'),
    mpatches.Patch(color='yellow', label='Moderate (51-100)'),
    mpatches.Patch(color='orange', label='Unhealthy for Sensitive Groups (101-150)'),
    mpatches.Patch(color='red', label='Unhealthy (151-200)'),
    mpatches.Patch(color='purple', label='Very Unhealthy (201-300)'),
    mpatches.Patch(color='maroon', label='Hazardous (301+)')
]

plt.legend(handles=legend_patches, title='AQI Categorieën', loc='upper right')

plt.tight_layout()
plt.show()
