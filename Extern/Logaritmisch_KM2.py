import pandas as pd
import matplotlib.pyplot as plt

region_areas = {
    'Asia Pacific': 41600000,
    'Russia & Caspian': 17100000,
    'Central and South America': 17800000,
    'North America': 24700000,
    'Europe': 10180000,
    'Africa': 30370000,
    'Middle East': 7500000
}

EmissionAbsoluteDF = pd.read_csv('emissionabsolute.csv', delimiter=',')

region_emissions_sum = EmissionAbsoluteDF.groupby('region_x')['emissions'].sum().reset_index()

region_emissions_sum['Area (km²)'] = region_emissions_sum['region_x'].map(region_areas)

region_emissions_sum['Emissions per km²'] = region_emissions_sum['emissions'] / region_emissions_sum['Area (km²)']

region_emissions_sum = region_emissions_sum.sort_values(by='Emissions per km²', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(region_emissions_sum['region_x'], region_emissions_sum['Emissions per km²'], color='skyblue')

plt.xlabel('Regio')
plt.ylabel('Emissie per km²')
plt.title('Emissie per km² per Regio (Logarithmische Schaal)')

plt.yscale('log')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()