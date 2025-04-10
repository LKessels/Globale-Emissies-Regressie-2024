import pandas as pd
import matplotlib.pyplot as plt

pastels = ['#EF476F', '#F78C6B', '#FFD166', '#06D6A0', '#118AB2', '#073B4C']

grouped_data = CompleteRegion_DF.groupby(['region', 'aqi category']).size().unstack(fill_value=0)

normalized_data = grouped_data.div(grouped_data.sum(axis=1), axis=0)

ax = normalized_data.plot(kind='bar', stacked=True, figsize=(12, 6), color=pastels)

totals = grouped_data.sum(axis=1)
for i, total in enumerate(totals):
    ax.text(i, 0, total, ha='center', va='top')

plt.title('100% Stacked Bar Plot over AQI Categorieën per Regio')
plt.xlabel('Regio')
plt.ylabel('Percentage Steden')
plt.ylim(0, 1)
plt.yticks([0, 0.25, 0.5, 0.75, 1], ['0%', '25%', '50%', '75%', '100%'])
plt.xticks(rotation=45)

plt.tight_layout(pad=2)
plt.legend(title='AQI Categorie', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()