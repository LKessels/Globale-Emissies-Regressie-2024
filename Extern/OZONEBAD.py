import pandas as pd

PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')


Ozonefiltered_df = PlaceComplete_DF[~PlaceComplete_DF['ozone aqi category'].isin(['Good', 'Moderate', 'Unhealthy', 'Unhealthy for Sensitive Groups'])]


region_country_city_count = Ozonefiltered_df.groupby(['region', 'country'])['city'].nunique().reset_index(name='Aantal Landen')


total_cities = region_country_city_count['Aantal Landen'].sum()
region_country_city_count['Percentage'] = ((region_country_city_count['Aantal Landen'] / total_cities) * 100).round(2).astype(str) + '%'


region_country_city_count.columns = ['Regio', 'Land', 'Aantal Landen', 'Percentage']


styled_table = region_country_city_count.style.set_caption("Aantal Steden met een Erg Ongezonde Ozone AQI-Categorisatie").set_table_styles(
    [{'selector': 'th', 'props': [('font-weight', 'bold'), ('text-align', 'center')]},
     {'selector': 'td', 'props': [('text-align', 'center')]},
     {'selector': 'caption', 'props': [('caption-side', 'top'), ('text-align', 'left'), ('font-weight', 'bold'), ('min-width', '500px'), ('white-space', 'nowrap')]},
     {'selector': 'tr', 'props': [('border', 'none')]},
     {'selector': 'index', 'props': [('display', 'none')]},
    ]
)

display(styled_table)
