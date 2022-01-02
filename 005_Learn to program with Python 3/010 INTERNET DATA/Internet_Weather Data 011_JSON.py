# INTERNET DATA - JSON

import os, json, urllib.request as urlRe
os.system('cls')

# API key provided from http://openweathermap.org/API
API_KEY = '53dc38be76a9813295dde8dc69ad9daa'

def getInfo(city):
    urlAndParams = f'http://api.openweathermap.org/data/2.5/weather?q={city}&mode=json&APPID={API_KEY} '
      
    print(f'\nSending URL: {urlAndParams}')

    # open the URL
    connection = urlRe.urlopen(urlAndParams)
    
    # Make a request and save the response as string
    responseString = connection.read()
    print(responseString)
    
    '''
    {'coord': {'lon': 15.9775, 'lat': 45.8131}, 
    'weather': [{'id': 800,
        'main': 'Clear',
        'description': 'clear sky', 
        'icon': '01d'}], 
    'base': 'stations', 
            'main': {'temp': 282.65,
            'feels_like': 282.65, 
            'temp_min': 280.97, 
            'temp_max': 283.65, 
            'pressure': 1021, 
            'humidity': 83}, 
            'visibility': 10000, 
            'wind': {'speed': 0.51, 'deg': 0}, 
            'clouds': {'all': 0}, 
            'dt': 1641123261, 
            'sys': {'type': 2, 
            'id': 2006646, 
            'country': 'HR', 
            'sunrise': 1641105439, 
            'sunset': 1641136945}, 
            'timezone': 3600, 
            'id': 6618983, 
            'name': 'Donji grad', 
            'cod': 200}
    '''
    
    responseDict = json.loads(responseString) # Convert from JSON to Python dictionary
    # print(responseDict)
    
    mainDict = responseDict['main'] # Get info associated with the main key
    
    degrees = mainDict['temp'] # Get the temperature from that dictionary
    
    return float(degrees)
   

# Convert K to °C
def convertKtoC(degreesK):
    degreesC = degreesK - 273.15
    return degreesC

while True:
    city = input('\nEnter a city (or press ENTER to quit): ').capitalize()
    if city == '':
        break
    tempK = getInfo(city)
    # Temperature conversion
    tempC = convertKtoC(tempK)        
    print(f'\nThe temperature of {city} is {round(tempC, 1)}°C\n')


print('\nFAREWELL!\n')
    
    
        
    