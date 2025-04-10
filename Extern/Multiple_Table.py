import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Metric': ['Slope (m)', 'Intercept (c)', 'Mean Squared Error', 'R^2 Score', 'Trend'],
    'Asia Pacific': [0.002144698057376348, 115.49496991493993, 1926.8275129768256, 1.1933581204881527e-05, 'Upwards'],
    'Other Regions': [0.1223960765098442, 52.52891036609837, 109.4224128015783, 0.04969346576900102, 'Upwards']
}

regression_results_df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(8, 4))  # Set the size of the table
ax.axis('tight') 
ax.axis('off')

table = ax.table(cellText=regression_results_df.values, colLabels=regression_results_df.columns, loc='center', cellLoc='center', colLoc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
table.auto_set_column_width([0, 1, 2])

plt.show()