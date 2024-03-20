#
# Uzdevums:
# Izmantojot piemēru no pirma uzdevuma, izveidojiet programmu kas atspoguļos laika apstakļus (temperaturu un nokrišņus) pa stundām 
# izmantojot sekojošu datu linku 
# https://api.open-meteo.com/v1/forecast?latitude={lat}.8&longitude={lon}.2&hourly=temperature_2m,precipitation&forecast_days=1
# 
import urllib.request
import json
from statistics import mean 

def get_weather_information(lat, lon):
    link = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation&forecast_days=1"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

def display_weather_information(weather_info):
    x = 0
    if weather_info:
        print("Weather Information:")
        hours = weather_info['hourly']['time']
        temperature = weather_info['hourly']['temperature_2m']
        precipitation = weather_info['hourly']['precipitation']

        for i in hours: 
            print("Time: ",i)
            print("Temperature: ",temperature[x])
            print("Precipitation: ",precipitation[x])
            print("---------------------")
            x+=1
        
        
    else:
        print("No city information available.")

lat = "56.8"
lon = "24.2"
weather_information = get_weather_information(lat, lon)
display_weather_information(weather_information)