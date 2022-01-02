import os
os.system('cls')

# Creating a dictionary {key1 : value1, key2 : value2, ...}

houseDict = {'color' : 'blue', 'style' : 'colonial', 'numberOfBedrooms' : 4,\
    'garage' : True, 'burglarAlarm' : False, 'streetNumber' : 123,\
    'streetName' : 'Any street', 'city' : 'Anytown', 'state' : 'CA',\
    'price': 625000}

print(houseDict)
print()
print(houseDict['color'])
print()
print(houseDict['state'])
print()
print(houseDict['numberOfBedrooms'])

print()

houseDict['price'] = 575000
print(houseDict)

print()

houseDict['numberOfBathrooms'] = 2.5
print(houseDict)

print()

print(houseDict.keys())
print()
print(houseDict.values())
print()

print(houseDict['streetName'])
print()
#print(houseDict['roofType'])
print('city' in houseDict)
print()
print('roofType' in houseDict)
print()

