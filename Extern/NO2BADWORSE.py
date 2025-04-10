import pandas as pd

PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')

filtered_df = PlaceComplete_DF[
    (PlaceComplete_DF['no2 aqi category'] != 'Good') & 
    (~PlaceComplete_DF['country'].isin(['China', 'Indonesia']))
]

region_country_no2_aqi = filtered_df.groupby(['region', 'country'])['no2 aqi value'].mean().reset_index(name='NO2 AQI Waarde')

region_country_no2_aqi['NO2 AQI Waarde'] = region_country_no2_aqi['NO2 AQI Waarde'].round(0).astype(int)

region_country_no2_aqi = region_country_no2_aqi.sort_values(by='NO2 AQI Waarde', ascending=True)

region_country_no2_aqi.columns = ['Regio', 'Land', 'NO2 AQI Waarde']

region_country_no2_aqi.reset_index(drop=True, inplace=True)

styled_table = region_country_no2_aqi.style.set_caption("NO2 AQI Waarde per Land en Regio")
styled_table = styled_table.set_table_styles(
    [{'selector': 'th', 'props': [('font-weight', 'bold'), ('text-align', 'center')]},
     {'selector': 'td', 'props': [('text-align', 'center')]}]
)

display(styled_table)
