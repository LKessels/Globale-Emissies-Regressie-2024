import pandas as pd
from IPython.display import display, HTML

data = {
    'Kolom Naam': ['Region', 'Country', 'Emissions', 'Type', 'Segment', 'Reason', 'baseYear', 'Notes'],
    'Data Type': ['String', 'String', 'Float', 'String', 'String', 'String', 'String', 'String'],
    'Voorbeeld': ['Africa', 'France', '5.2E+14', 'Energy', 'Bioenergy', 'Vented', '2022', 'Not Available']
}

MethaneTableDF = pd.DataFrame(data)

MethaneStyled_df = MethaneTableDF.style.set_table_styles([
    {'selector': 'th', 'props': [('font-weight', 'bold')]},
    {'selector': 'td', 'props': [('border', '1px solid black')]},
    {'selector': 'table', 'props': [('border-collapse', 'collapse')]}
])

MethaneStyled_df.hide(axis='index')

html_title = "<h2 style='text-align:left;'>Globale Emissie Data Tabel</h2>"

display(HTML(html_title + MethaneStyled_df.to_html()))