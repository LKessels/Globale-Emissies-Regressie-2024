import pandas as pd
import numpy as np

bins = [150, 160, 170, 180, 190, 200]
reasons = ['All', 'Fugitive', 'Vented', 'Flared']

frequency_data = {}

for reason in reasons:
    reason_data = energy_data[energy_data['reason'] == reason]
    frequencies, edges = np.histogram(reason_data['aqi value'], bins=bins)
    frequency_data[reason] = frequencies

frequency_df = pd.DataFrame(frequency_data, index=[f'{bins[i]}-{bins[i+1]-1}' for i in range(len(bins)-1)])

total_frequencies = frequency_df.sum(axis=1)

frequency_percent_df = frequency_df.div(total_frequencies, axis=0) * 100

frequency_percent_df = frequency_percent_df.round(1)

import IPython.display as display
frequency_percent_df = frequency_percent_df.reset_index()

frequency_percent_df.columns = ['AQI Range', 'All (%)', 'Fugitive (%)', 'Vented (%)', 'Flared (%)']
display.display(frequency_percent_df)