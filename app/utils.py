import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}


def get_weather_data(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    res = requests.get(url, headers=headers)
    print(url, res.content)
    data = res.json()
    main_data = data['properties']['timeseries'][0]
    time = main_data['time']
    air_pressure_at_sea_level = main_data['data']['instant']['details']['air_pressure_at_sea_level']
    air_temperature = main_data['data']['instant']['details']['air_temperature']
    cloud_area_fraction = main_data['data']['instant']['details']['cloud_area_fraction']
    relative_humidity = main_data['data']['instant']['details']['relative_humidity']
    wind_from_direction = main_data['data']['instant']['details']['wind_from_direction']
    wind_speed = main_data['data']['instant']['details']['wind_speed']
    next_1_hours_summary = main_data['data']['next_1_hours']['summary']['symbol_code']
    output_data = {
        'time': time,
        'air_pressure_at_sea_level': air_pressure_at_sea_level,
        'air_temperature': air_temperature,
        'cloud_area_fraction': cloud_area_fraction,
        'relative_humidity': relative_humidity,
        'wind_from_direction': wind_from_direction,
        'wind_speed': wind_speed,
        'next_1_hours_summary': next_1_hours_summary,
    }
    return output_data
