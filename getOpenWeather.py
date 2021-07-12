#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
APPID = 'e140ecd12976bae5b6936eb9dc07b1ea'

import json,requests,sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

#Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)


# Load JSON data in to a python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print('Temp:',round(w[0]['main']['temp'] - 273.15,1),'degC')
print(w[0]['weather'][0]['main'] + ':',w[1]['weather'][0]['description'])
print('Wind speed:',w[0]['wind']['speed'],)
print()
print('Tomorrow:')
print('Temp:',round(w[1]['main']['temp'] - 273.15,1),'degC')
print(w[1]['weather'][0]['main'] + ':', w[1]['weather'][0]['description'])
print('Wind speed:',w[1]['wind']['speed'],)
print()
print('Day after tomorrow:')
print('Temp:',round(w[2]['main']['temp'] - 273.15, 1),'degC')
print(w[2]['weather'][0]['main'] + ':', w[2]['weather'][0]['description'])
print('Wind speed:',w[2]['wind']['speed'],)
