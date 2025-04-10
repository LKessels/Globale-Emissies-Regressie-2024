import pandas as pd

EmissionAbsoluteDF = pd.read_csv('emissionabsolute.csv', delimiter=',')

region_reason_emissions = EmissionAbsoluteDF.groupby(['region_x', 'reason'])['emissions'].sum().unstack().reset_index()

region_reason_emissions.set_index('region_x', inplace=True)

reason_order = ['All', 'Fugitive', 'Vented', 'Flared']
region_reason_emissions = region_reason_emissions[reason_order]

region_total_emissions = region_reason_emissions.sum(axis=1)

region_reason_percent = region_reason_emissions.divide(region_total_emissions, axis=0) * 100

region_reason_percent = region_reason_percent.round(2)

region_reason_percent = region_reason_percent.reset_index()

region_reason_percent.columns = ['Regio', 'All (%)', 'Fugitive (%)', 'Vented (%)', 'Flared (%)']
import IPython.display as display
display.display(region_reason_percent)