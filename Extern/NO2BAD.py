import pandas as pd

PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')

filtered_df = PlaceComplete_DF[PlaceComplete_DF['no2 aqi category'] != 'Good']

display(filtered_df)