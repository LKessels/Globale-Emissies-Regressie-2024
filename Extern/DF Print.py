import pandas as pd

AirPollutionDF = pd.read_csv('global air pollution dataset.csv')
MethaneDF = pd.read_csv('Methane_final.csv')

def adjust_width(column, width):
    return column.apply(lambda x: str(x).ljust(width)[:width])

AirPollutionDF['Country'] = adjust_width(AirPollutionDF['Country'], 20)
AirPollutionDF['City'] = adjust_width(AirPollutionDF['City'], 25)
AirPollutionDF['AQI Value'] = adjust_width(AirPollutionDF['AQI Value'].astype(str), 11)
AirPollutionDF['AQI Category'] = adjust_width(AirPollutionDF['AQI Category'], 40)

MethaneDF['region'] = adjust_width(MethaneDF['region'], 20)
MethaneDF['emissions'] = adjust_width(MethaneDF['emissions'], 25)
MethaneDF['type'] = adjust_width(MethaneDF['type'], 11)
MethaneDF['segment'] = adjust_width(MethaneDF['segment'], 40)

airpollution_columns = ['Country', 'City', 'AQI Value', 'AQI Category']
methane_columns = ['region', 'emissions', 'type', 'segment']

def print_centered(df, columns):
    total_length = sum([len(str(df[col][0])) for col in columns])
    
    screen_width = 120
    space = (screen_width - total_length) // 2
    
    header_str = ''.join(f'{col:<20}' for col in columns)
    print(' ' * space + header_str)
    
    print(' ' * space + '-' * total_length)
    
    for _, row in df[columns].head().iterrows():
        row_str = ''.join(f'{str(val):<20}' for val in row)
        print(' ' * space + row_str)

print("Air Pollution DataFrame:")
print_centered(AirPollutionDF, airpollution_columns)

print("\nMethane Emissions DataFrame:")
print_centered(MethaneDF, methane_columns)