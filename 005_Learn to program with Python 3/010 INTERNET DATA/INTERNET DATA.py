# INTERNET DATA

# Getting a stock quote
import urllib.request

# api key provided from www.alphavantage.co
API_KEY = '53dc38be76a9813295dde8dc69ad9daa'

def getInfo(city):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&mode=xml&APPID={API_KEY} '
      
    print(f'\nSending URL: {URL}')

    # open the URL
    connection = urllib.request.urlopen(URL)
    
    # read and convert bytes to a string
    responseString = connection.read().decode()
    
    print(f'\nResponse is: {responseString}')
    
    # Look for a prefix in the response
    prefixString = '<temperature value="'
    
    # do a little math to figure out start and end index of the real price:
    prefixStringLength = len(prefixString)
    prefixStringPosition = responseString.index(prefixString)
    
    start = prefixStringPosition + prefixStringLength
    end = responseString.index('"', start)
    
    # extract the temperature using a slice and return it
    degreesK = float(responseString[start : end])
    return degreesK

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
    print(f'\nThe temperature of {city} is {tempC}°C\n')

print('\nFAREWELL!\n')
    
    
        
    