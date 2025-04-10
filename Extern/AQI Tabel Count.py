import pandas as pd

table_data = CompleteRegion_DF.groupby(['region', 'aqi category']).size().unstack(fill_value=0)

styled_table = table_data.style.set_caption("Aantal Steden per AQI Categorie en Regio") \
                              .set_table_styles([{
                                  'selector': 'table',
                                  'props': [('border-collapse', 'collapse')]
                              }, {
                                  'selector': 'th, td',
                                  'props': [('border', '2px solid black'),
                                            ('text-align', 'center')]
                              }]) \
                              .format(precision=0)

styled_table