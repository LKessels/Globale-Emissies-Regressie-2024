import pandas as pd
import matplotlib.pyplot as plt

EmissionAbsoluteDF = pd.read_csv('emissionabsolute.csv', delimiter=',')

region_type_emissions = EmissionAbsoluteDF.groupby(['region_x', 'type'])['emissions'].sum().unstack().reset_index()

ax = region_type_emissions.plot(kind='bar', stacked=True, figsize=(10, 7))

plt.title('Totale Emissie per Regio per Emissietype (Log Schaal)', fontsize=16)
plt.xlabel('Regio', fontsize=12)
plt.ylabel('Totale Emissie (kiloton)', fontsize=12)

plt.yscale('log')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()