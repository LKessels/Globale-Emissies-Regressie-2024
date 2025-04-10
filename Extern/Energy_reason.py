import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

energy_data = MergedDatasetsDF[MergedDatasetsDF['type'] == 'Energy'][['aqi value', 'aqi category', 'reason']].copy()

bins = range(0, 361, 10)

reasons = energy_data['reason'].unique()

plt.figure(figsize=(10, 6))

reason_colors = ['lavenderblush', 'orchid', 'purple', 'mediumorchid']

for i, reason in enumerate(reasons):
    reason_data = energy_data[energy_data['reason'] == reason]
    plt.hist(reason_data['aqi value'], bins=bins, edgecolor='black', alpha=0.7, label=reason, color=reason_colors[i])

plt.title('Distribution of AQI Values for Energy Type by Reason', fontsize=14)
plt.xlabel('AQI Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

legend_patches = [mpatches.Patch(color=color, label=reason) for reason, color in zip(reasons, reason_colors)]

plt.legend(handles=legend_patches, title='Reason', loc='upper right')

plt.tight_layout()
plt.show()