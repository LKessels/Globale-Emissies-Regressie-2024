import pandas as pd
from IPython.display import display, HTML

AirPollutionDF = pd.read_csv('global air pollution dataset.csv')
MethaneDF = pd.read_csv('Methane_final.csv')

# kleine letters
AirPollutionDF.columns = AirPollutionDF.columns.str.lower()

#mapping
country_to_region = MethaneDF.set_index('country')['region'].to_dict()

# Map toepassen
AirPollutionDF['region'] = AirPollutionDF['country'].map(country_to_region)

# Landen zonder regio
missing_regions = AirPollutionDF[AirPollutionDF['region'].isnull()]['country'].unique()

# Kolommen functie
def reshape_missing_regions(missing_regions, max_columns=12):
    # Calculate the number of rows needed
    num_rows = (len(missing_regions) + max_columns - 1) // max_columns
    
    reshaped_df = pd.DataFrame(index=range(num_rows), columns=range(max_columns))
    
    
    for i, country in enumerate(missing_regions):
        row = i // max_columns
        col = i % max_columns
        reshaped_df.iat[row, col] = country
        
    
    reshaped_df.columns = [''] * max_columns
    return reshaped_df

# Toepassen van functie
missing_regions_df = reshape_missing_regions(missing_regions)

# Nieuw Dataframe gesorteerd
sorted_air_pollution_df = AirPollutionDF.sort_values(by=['region', 'country']).head(5)

# tabel
print("Voorbeeld van gesorteerde AQI-waardes gebaseerd op regio:")
display(HTML(sorted_air_pollution_df.to_html(index=False)))

print("Landen zonder gekoppelde regio:")
display(HTML(missing_regions_df.to_html(index=False)))