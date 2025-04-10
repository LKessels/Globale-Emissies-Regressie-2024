import pandas as pd

PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')

filtered_df = PlaceComplete_DF[PlaceComplete_DF['co aqi category'] != 'Good']

styled_table = filtered_df.style.set_caption("Rows Excluding 'Good' CO AQI Category") \
                                 .set_table_styles([{
                                     'selector': 'table',
                                     'props': [('border-collapse', 'collapse')]
                                 }, {
                                     'selector': 'th, td',
                                     'props': [('border', '1px solid black'),
                                               ('text-align', 'center'),
                                               ('padding', '8px')]
                                 }, {
                                     'selector': 'th',
                                     'props': [('background-color', '#f2f2f2')]
                                 }]) \
                                 .format(na_rep='Not Available')

styled_table