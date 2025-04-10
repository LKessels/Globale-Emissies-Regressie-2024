import pandas as pd

region_areas = {
    'Asia Pacific': 41600000,
    'Russia & Caspian': 17100000,
    'Central and South America': 17800000,
    'North America': 24700000,
    'Europe': 10180000,
    'Africa': 30370000,
    'Middle East': 7500000
}

region_area_df = pd.DataFrame(list(region_areas.items()), columns=['Regio', 'Grootte (km²)'])

region_area_df = region_area_df.sort_values(by='Grootte (km²)', ascending=False)

import IPython.display as display
display.display(region_area_df)