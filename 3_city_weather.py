#
# Uzdevums:
# Apvienojiet divas programmas. Atspoguļojiet laika apstākļus katrai stundai, pilsētai kuru ievada lietotājs.
# Pilsētas koordinātes paņemiet ar pirmo pieprasījumu (pirmu rezultātu) un laika apstākļus pieprasiet ar dotam koordinātem
#
import urllib.request
import json

def get_city_information(city):
    link = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=3&language=lv&format=json"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

def get_city_latandlong(city_info):
    if city_info:
        latitude = city_info['results'][0]['latitude']
        longtitude = city_info['results'][0]['longitude']
        return latitude, longtitude
            
    else:
        print("No city information available.")


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

city_name = input("Enter city name: ")
if len(city_name) >= 2:
    city_information = get_city_information(city_name)
    lat = get_city_latandlong(city_information)[0]
    lon = get_city_latandlong(city_information)[1]
    weather_information = get_weather_information(lat, lon)
    display_weather_information(weather_information)