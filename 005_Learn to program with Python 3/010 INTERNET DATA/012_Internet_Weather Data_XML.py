# INTERNET DATA - XML

import os
import urllib.request as urlRe
import xml.etree.cElementTree as eTree
os.system('cls')

# API key provided from http://openweathermap.org/API
API_KEY = '53dc38be76a9813295dde8dc69ad9daa'

def getInfo(city):
    
    urlWithParams = f'http://api.openweathermap.org/data/2.5/weather?q={city}&mode=xml&APPID={API_KEY} '
      
    print(f'\nSending URL: {urlWithParams}')

    # Open the URL and save the response as an XML-formatted string
    connection = urlRe.urlopen(urlWithParams)
    
    # Read the response data and convert to a string
    responseString = connection.read().decode()
    
    print(responseString)
    
    '''
    <current>
        <city id="6618983" name="Donji grad">
            <coord lon="15.9775" lat="45.8131"></coord>
            <country>HR</country>
            <timezone>3600</timezone>
            <sun rise="2022-01-02T06:37:19" set="2022-01-02T15:22:25"></sun>
        </city>
            <temperature value="283.69" min="281.97" max="285.27" unit="kelvin"></temperature>
            <feels_like value="282.86" unit="kelvin"></feels_like>
            <humidity value="79" unit="%"></humidity>
            <pressure value="1020" unit="hPa"></pressure>
            <wind>
                <speed value="0.51" unit="m/s" name="Calm"></speed>
                <gusts></gusts>
                <direction></direction>
            </wind>
            <clouds value="0" name="clear sky"></clouds>
            <visibility value="10000"></visibility>
            <precipitation mode="no"></precipitation>
            <weather number="800" value="clear sky" icon="01d"></weather>
            <lastupdate value="2022-01-02T12:25:12"></lastupdate>
    </current>
    '''
    
    # Turn the string into an XML document
    tree = eTree.fromstring(responseString)
        
    # Find the temperature node (tag), then get the valu attribute inside it   
    temperatureInfo = tree.find('temperature')   
    degrees = temperatureInfo.attrib['value']
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
    
    
        
    