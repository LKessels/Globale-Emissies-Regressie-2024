missing_cities = AQI_Region_DF[AQI_Region_DF['country'].isnull()]['city'].unique()

def reshape_missing_cities(missing_cities, max_columns=12, max_rows=3):
    
    num_rows = min((len(missing_cities) + max_columns - 1) // max_columns, max_rows)
    reshaped_df = pd.DataFrame(index=range(num_rows), columns=range(max_columns))
    
    for i, city in enumerate(missing_cities):
        if i >= num_rows * max_columns:
            break
        row = i // max_columns
        col = i % max_columns
        reshaped_df.iat[row, col] = city
        
    reshaped_df.columns = [''] * max_columns
    return reshaped_df

missing_cities_df = reshape_missing_cities(missing_cities)

missing_cities_df.index = [''] * len(missing_cities_df)
display(missing_cities_df)