
import pandas as pd

# Lae elektrihindade graafikud

source_data = pd.read_json(r'C:\Users\opilane\Desktop\Andmetarkus,git\Andmetarkus\Python\Day3\el_data_2024.json')
electricity_data = pd.json_normalize(source_data["data"])
print(electricity_data.head())

source_data_2 = pd.read_csv(r'C:\Users\opilane\Desktop\Andmetarkus,git\Andmetarkus\Python\Day3\tallinn_harku_2024.csv')
weather_data = pd.DataFrame(source_data_2)
print(weather_data.head())

weather_data['datetime'] = pd.to_datetime(
    weather_data['Aasta'].astype(str) + '-' +
    weather_data['Kuu'].astype(str).str.zfill(2) + '-' +
    weather_data['Päev'].astype(str).str.zfill(2) + ' '+
    weather_data['Kell (UTC)'].astype(str).str[:5]
)
print(weather_data.head())

# Ühenda andmed kuupäeva alusel
# merged_data = pd.merge(electricity_data, weather_data, on='datetime', how='inner')
# print(merged_data.head())