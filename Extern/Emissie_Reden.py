import pandas as pd
import matplotlib.pyplot as plt

EmissionAbsoluteDF = pd.read_csv('emissionabsolute.csv', delimiter=',')

region_reason_emissions = EmissionAbsoluteDF.groupby(['region_x', 'reason'])['emissions'].sum().unstack().reset_index()

region_reason_emissions.set_index('region_x', inplace=True)

reason_order = ['All', 'Fugitive', 'Vented', 'Flared']
region_reason_emissions = region_reason_emissions[reason_order]

reason_colors = ['lavenderblush', 'orchid', 'purple', 'mediumorchid']

ax = region_reason_emissions.plot(kind='bar', stacked=True, figsize=(10, 7), color=reason_colors, edgecolor='black')

plt.title('Totale Emissie per Regio per Emissiereden (Log Scale)', fontsize=16)
plt.xlabel('Regio', fontsize=12)
plt.ylabel('Totale Emissie (kiloton)', fontsize=12)

plt.yscale('log')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
