import pandas as pd

reason_distribution_normalized = reason_distribution_normalized.round(1)

region_reason_percent = reason_distribution_normalized.reset_index()

region_reason_percent.columns = ['AQI Bin', 'All (%)', 'Fugitive (%)', 'Vented (%)', 'Flared (%)']

import IPython.display as display
display.display(region_reason_percent)
