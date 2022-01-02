import os
os.system('cls')

personalDataDict = {
    'Joe' : {'height' : 73, 'weight' : 200, 'sex' : 'M', 'age' : 35,
             'allergies' : ['tree pollen', 'carrots', 'onions']},\
    'Sally' : {'height' : 58, 'weight' : 100, 'sex' : 'F', 'age' : 32,
             'allergies' : ['bee stings']},\
    'John' : {'height' : 36, 'weight' : 75, 'sex' : 'M', 'age' : 8,
             'allergies' : ['peanuts']},\
    'Mary' : {'height' : 35, 'weight' : 60, 'sex' : 'F', 'age' : 7,
             'allergies' : []},\
}

joesData = personalDataDict['Joe']
joesAllergies = joesData['allergies']
print(joesAllergies)


marysData = personalDataDict['Mary']
marysAllergies = marysData['allergies']
print(marysAllergies)

for personName in personalDataDict:
    onePersonDict = personalDataDict[personName]
    allergyList = onePersonDict['allergies']
    
    if allergyList == []:
        print(f'\n{personName} is not allergic to anything')
    else:
            print(f'\n{personName} is allergic to {allergyList}')
