import pandas as pd


category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

PlaceComplete_DF['pm2.5 aqi category'] = pd.Categorical(
    PlaceComplete_DF['pm2.5 aqi category'], 
    categories=category_order, 
    ordered=True
)

grouped_data = PlaceComplete_DF.groupby(['region', 'pm2.5 aqi category']).size().unstack(fill_value=0)

percent_distribution = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
percent_distribution = percent_distribution.round(2)

percent_distribution.columns = [f'{category} (%)' for category in category_order]

styled_table = (
    percent_distribution.style
    .set_caption("Percentage Distribution of PM2.5 AQI Categories per Region")
    .format("{:.2f}%")
    .set_properties(**{'text-align': 'center'})  # Center-align text
    .set_table_styles([
        {'selector': 'th', 'props': [('border', '1px solid black'), ('font-weight', 'bold'), ('text-align', 'center')]},
        {'selector': 'td', 'props': [('border', '1px solid black')]}
    ])
)

styled_table
