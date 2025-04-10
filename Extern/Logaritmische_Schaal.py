import pandas as pd
import matplotlib.pyplot as plt

EmissionAbsoluteDF = pd.read_csv('emissionabsolute.csv', delimiter=',')

region_emissions_sum = EmissionAbsoluteDF.groupby('region_x')['emissions'].sum().reset_index()

region_emissions_sum = region_emissions_sum.sort_values(by='emissions', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(region_emissions_sum['region_x'], region_emissions_sum['emissions'], color='skyblue')

plt.yscale('log')

plt.xlabel('Regio')
plt.ylabel('Totale Emissie (Ton)')
plt.title('Totale emissie per Region (Logaritmische Schaal)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
