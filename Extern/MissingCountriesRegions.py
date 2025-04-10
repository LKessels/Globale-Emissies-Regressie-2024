import pandas as pd
from IPython.display import display, HTML

AirPollutionDF = pd.read_csv('global air pollution dataset.csv')
MethaneDF = pd.read_csv('Methane_final.csv')

AirPollutionDF.columns = AirPollutionDF.columns.str.lower()

country_to_region = MethaneDF.set_index('country')['region'].to_dict()

AirPollutionDF['region'] = AirPollutionDF['country'].map(country_to_region)

missing_regions = AirPollutionDF[AirPollutionDF['region'].isnull()]['country'].unique()

def reshape_missing_regions(missing_regions, max_columns=12):
    num_rows = (len(missing_regions) + max_columns - 1) // max_columns
    reshaped_df = pd.DataFrame(index=range(num_rows), columns=range(max_columns))
    
    for i, country in enumerate(missing_regions):
        row = i // max_columns
        col = i % max_columns
        reshaped_df.iat[row, col] = country
        
    reshaped_df.columns = [''] * max_columns
    return reshaped_df

missing_regions_df = reshape_missing_regions(missing_regions)

missing_country_to_region = {
    'Russian Federation': 'Russia & Caspian',
    'United States of America': 'North America',
    'Belgium': 'Europe',
    'Republic of North Macedonia': 'Europe',
    'Finland': 'Europe',
    'United Kingdom of Great Britain and Northern Ireland': 'Europe',
    'United Republic of Tanzania': 'Africa',
    'Haiti': 'North America',
    'Latvia': 'Europe',
    'Viet Nam': 'Asia Pacific',
    'Iran (Islamic Republic of)': 'Asia Pacific',
    'El Salvador': 'North America',
    'Bulgaria': 'Europe',
    'Guatemala': 'North America',
    'Ireland': 'Europe',
    'Turkey': 'Asia Pacific',
    'Democratic Republic of the Congo': 'Africa',
    'Switzerland': 'Europe',
    'Portugal': 'Europe',
    "Côte d'Ivoire": 'Africa',
    'Hungary': 'Europe',
    'Spain': 'Europe',
    'Myanmar': 'Asia Pacific',
    'Papua New Guinea': 'Oceania',
    'Madagascar': 'Africa',
    'Lithuania': 'Europe',
    'Armenia': 'Asia Pacific',
    'Serbia': 'Europe',
    'Slovakia': 'Europe',
    'Bosnia and Herzegovina': 'Europe',
    'Czechia': 'Europe',
    'Dominican Republic': 'North America',
    'Bolivia (Plurinational State of)': 'Central and South America',
    'Chile': 'Central and South America',
    'Panama': 'North America',
    'Kyrgyzstan': 'Asia Pacific',
    'Mauritius': 'Africa',
    'Greece': 'Europe',
    'Malawi': 'Africa',
    'Albania': 'Europe',
    'Lesotho': 'Africa',
    'Venezuela (Bolivarian Republic of)': 'Central and South America',
    'Solomon Islands': 'Oceania',
    'Zimbabwe': 'Africa',
    'Austria': 'Europe',
    'Croatia': 'Europe',
    'Honduras': 'North America',
    'Cambodia': 'Asia Pacific',
    'Uganda': 'Africa',
    'Republic of Moldova': 'Europe',
    'Kingdom of Eswatini': 'Africa',
    'Afghanistan': 'Asia Pacific',
    'Zambia': 'Africa',
    'Belarus': 'Europe',
    'Malta': 'Europe',
    'Rwanda': 'Africa',
    'Sri Lanka': 'Asia Pacific',
    'Burundi': 'Africa',
    'Jamaica': 'North America',
    'Mali': 'Africa',
    'Costa Rica': 'North America',
    'Nicaragua': 'North America',
    'Republic of Korea': 'Asia Pacific',
    'Burkina Faso': 'Africa',
    'Cabo Verde': 'Africa',
    'Mauritania': 'Africa',
    'Tajikistan': 'Asia Pacific',
    'Barbados': 'North America',
    'Syrian Arab Republic': 'Asia Pacific',
    "Lao People's Democratic Republic": 'Asia Pacific',
    'Bhutan': 'Asia Pacific',
    'Saint Lucia': 'North America',
    'Georgia': 'Asia Pacific',
    'Nepal': 'Asia Pacific',
    'Cyprus': 'Europe',
    'Montenegro': 'Europe',
    'Comoros': 'Africa',
    'Iceland': 'Europe',
    'Andorra': 'Europe',
    'Luxembourg': 'Europe',
    'Vanuatu': 'Oceania',
    'Aruba': 'North America',
    'Belize': 'North America',
    'Palau': 'Oceania',
    'Suriname': 'Central and South America',
    'Singapore': 'Asia Pacific',
    'Maldives': 'Asia Pacific',
    'State of Palestine': 'Asia Pacific',
    'Saint Kitts and Nevis': 'North America',
    'Monaco': 'Europe'
}

AirPollutionDF['region'] = AirPollutionDF['country'].map(missing_country_to_region).fillna(AirPollutionDF['region'])

sorted_updated_air_pollution_df = AirPollutionDF.sort_values(by=['region', 'country'])

selected_countries = ['Belgium', 'Portugal', 'Chile', 'Honduras', 'Afghanistan']
display_countries = sorted_updated_air_pollution_df[
    sorted_updated_air_pollution_df['country'].isin(selected_countries)
].drop_duplicates(subset='country')

display(display_countries)
