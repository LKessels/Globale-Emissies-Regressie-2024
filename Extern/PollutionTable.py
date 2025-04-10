import pandas as pd
from IPython.display import display, HTML

data_luchtvervuiling = {
    'Kolom Naam': ['Country', 'City', 'AQI Value', 'AQI Category', 'CO AQI Value', 'CO AQI Category',
                    'Ozone AQI Value', 'Ozone AQI Category', 'NO2 AQI Value', 'NO2 AQI Category',
                    'PM2.5 AQI Value', 'PM2.5 AQI Category'],
    'Data Type': ['String', 'String', 'Int', 'String', 'Int', 'String', 
                  'Int', 'String', 'Int', 'String', 'Int', 'String'],
    'Voorbeeld': ['France', 'Phoenix', '41', 'Good', '24', 'Moderate', '34', 'Unhealthy', '11', 'Good', '66', 'Good']
}

LuchtvervuilingTableDF = pd.DataFrame(data_luchtvervuiling)

styled_df_luchtvervuiling = LuchtvervuilingTableDF.style.set_table_styles([
    {'selector': 'th', 'props': [('font-weight', 'bold')]},
    {'selector': 'td', 'props': [('border', '1px solid black')]},
    {'selector': 'table', 'props': [('border-collapse', 'collapse')]}
])

styled_df_luchtvervuiling.hide(axis='index')

html_title_luchtvervuiling = "<h2 style='text-align:left;'>Globale Luchtvervuiling Data Tabel</h2>"

display(HTML(html_title_luchtvervuiling + styled_df_luchtvervuiling.to_html()))
