import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

energy_data = MergedDatasetsDF[MergedDatasetsDF['type'] == 'Energy'][['aqi value', 'aqi category', 'reason']].copy()

bins = range(0, 550, 50)
labels = [f'{i}-{i+50}' for i in range(0, 500, 50)]

energy_data['AQI Bin'] = pd.cut(energy_data['aqi value'], bins=bins, labels=labels, right=False)

reason_bin_counts = energy_data.groupby(['AQI Bin', 'reason']).size().unstack(fill_value=0)

reason_bin_percentages = reason_bin_counts.div(reason_bin_counts.sum(axis=1), axis=0) * 100

reason_bin_percentages = reason_bin_percentages.round(2)

plt.figure(figsize=(10, 7))

bar_colors = ['white' if reason != 'All' else 'mediumorchid' for reason in reason_bin_percentages.columns]

ax = reason_bin_percentages.plot(kind='bar', stacked=True, figsize=(10, 7), color=bar_colors, edgecolor='black', legend=False)

plt.title('Percentage Distribution of Reasons for AQI Bins (Flared Colored)', fontsize=16)
plt.xlabel('AQI Bins', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)

for i, reason in enumerate(reason_bin_percentages.columns):
    if reason == 'Vented':
        for j, bin in enumerate(reason_bin_percentages.index):
            height = reason_bin_percentages.loc[bin, reason]
            if height > 0:
                ax.text(j, height / 2, f'{height:.1f}%', ha='center', va='center', color='black')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()