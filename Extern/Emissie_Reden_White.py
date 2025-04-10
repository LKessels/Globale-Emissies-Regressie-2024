import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

energy_data = MergedDatasetsDF[MergedDatasetsDF['type'] == 'Energy'][['aqi value', 'reason']].copy()

bins = range(0, 361, 10)

reasons = ['All', 'Fugitive', 'Vented', 'Flared']
reason_colors = ['lavenderblush', 'orchid', 'purple', 'mediumorchid']

plt.figure(figsize=(10, 6))

for reason, color in zip(reasons, reason_colors):
    reason_data = energy_data[energy_data['reason'] == reason]
    frequencies, edges = np.histogram(reason_data['aqi value'], bins=bins)
    
    bar_colors = [
        color if 150 <= edges[i] < 200 else 'white'
        for i in range(len(edges) - 1)
    ]
    
    plt.bar(
        edges[:-1], frequencies, width=np.diff(edges), edgecolor='black',
        align='edge', color=bar_colors, label=reason, alpha=0.7
    )

plt.title('Distributie van AQI-Waardes voor Emissietype: Energie per Emissiereden', fontsize=14)
plt.xlabel('AQI-Waarde', fontsize=12)
plt.ylabel('Frequentie', fontsize=12)

legend_patches = [mpatches.Patch(color=color, label=reason) for reason, color in zip(reasons, reason_colors)]
plt.legend(handles=legend_patches, title='Reason', loc='upper right')

plt.tight_layout()
plt.show()