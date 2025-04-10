import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Daily AQI Color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'Levels of Concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'Values of Index': ['0 to 50', '51 to 100', '101 to 150', '151 to 200', '201 to 300', '301 and higher'],
    'Description of Air Quality': [
        'Air quality is satisfactory, and air pollution\nposes little or no risk.',
        'Air quality is acceptable. However, there\nmay be a risk for some people, particularly those\nwho are unusually sensitive to air pollution.',
        'Members of sensitive groups may experience\nhealth effects. The general public is less\nlikely to be affected.',
        'Some members of the general public may\nexperience health effects; members of sensitive\ngroups may experience more serious health effects.',
        'Health alert: The risk of health effects\nis increased for everyone.',
        'Health warning of emergency conditions:\neveryone is more likely to be affected.'
    ]
}

AQI_df = pd.DataFrame(data)

row_colors = ['#00E400', '#FFFF00', '#FF7E00', '#FF0000', '#8F3F97', '#7E0023']

fig, ax = plt.subplots(figsize=(12, 6))

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

table = ax.table(
    cellText=AQI_df.values,
    colLabels=AQI_df.columns,
    cellLoc='center',
    loc='center',
    bbox=[0.05, 0.2, 0.9, 0.6]
)

for i in range(len(AQI_df)):
    for j in range(len(AQI_df.columns)):
        table[(i + 1, j)].set_facecolor(row_colors[i])
        if AQI_df.iloc[i]['Daily AQI Color'] in ['Purple', 'Maroon']:
            table[(i + 1, j)].set_text_props(color='white')

table.auto_set_font_size(False)
table.set_fontsize(8)

table.auto_set_column_width([0, 2])

table.scale(1.0, 3)

plt.title("AQI Basics for Ozone and Particle Pollution", fontweight="bold", fontsize=14)

plt.show()