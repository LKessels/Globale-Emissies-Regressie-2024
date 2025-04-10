import pandas as pd

EmissionAbsoluteDF = pd.read_csv('emissionabsolute.csv', delimiter=',')

region_emissions_sum = EmissionAbsoluteDF.groupby('region_x')['emissions'].sum().reset_index()

region_emissions_sum = region_emissions_sum.sort_values(by='emissions', ascending=False)

region_emissions_sum.columns = ['Regio', 'Totale Emissie (Ton)']

from IPython.display import display

display(region_emissions_sum)
