import requests
import json
import os
from requests.api import get
from datetime import datetime

API_KEY = json.load(open('Secrets.json', 'rb'))['WEATHERAPI_KEY']

# Create dictionary with Weather Description keys & CSS Values
WEATHERCOLOR = {
    'light rain': 'cyan',
    'moderate rain': 'darkblue',
    'heavy intensity rain': 'blue',
    'very heavy rain': 'blue',
    'light snow': 'white',
    'snow': 'white',
    'clear sky': 'yellow'
}


def RedmondForecast():
    '''This function grabs the 7 day forecast for Redmond, WA'''

    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q": "redmond,us", "lat": "47.67", "lon": "-122.12",
                   "cnt": "7", "units": "imperial", "zip": "98053"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    response = requests.get(url, headers=headers, params=querystring)

    weatherapi = json.loads(response.text)

    forecast = weatherapi['list']

    # NOTE cycling through a loop and grabbing each of the variables I want.
    for i in range(len(forecast)):
        forecast[i] = {  # NOTE original forecast is ALL of the original variables (dt, weather, sunset, temp, etc), we are now ONLY grabbing specific variables
            # NOTE grabs from existing dictionary (dt) and then converts to datetime, and then converts to a string in my format (m d y), and recreates it as "day"
            'Day': datetime.fromtimestamp(forecast[i]['dt']).strftime('%m-%d-%y'),
            'Sunrise': datetime.fromtimestamp(forecast[i]['sunrise']).strftime('%I:%M %p'),
            'Sunset': datetime.fromtimestamp(forecast[i]['sunset']).strftime('%I:%M %p'),
            # NOTE grabbing values from existing dictionary
            'Day Temp': forecast[i]['temp']['day'],
            'Low Temp': forecast[i]['temp']['min'],
            'High Temp': forecast[i]['temp']['max'],
            'Weather': forecast[i]['weather'][0]['main'],
            'Weather Desc.': forecast[i]['weather'][0]['description'],
        }  # NOTE New forecast[i] = only the variables grabbed

    json.dump(forecast, open('Forecast.txt', 'w'), indent=2)

    return forecast
