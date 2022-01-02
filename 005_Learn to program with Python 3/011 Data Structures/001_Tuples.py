import os
os.system('cls')

friendsList = ['Romeo', 'Sunčana', 'Igor', 'Vlatka']
print(friendsList)
print(len(friendsList))
print(friendsList[0])
print(friendsList[3])

friendsList[2] = 'Saša'
print(friendsList)

friendsList.append('Ana')
print(friendsList)

friendsTuple = ('Romeo', 'Sunčana', 'Igor', 'Vlatka')
print(friendsTuple)
print(len(friendsTuple))
print(friendsTuple[0])
print(friendsTuple[3])

# friendsTuple[2] = 'Saša'
# print(friendsTuple)

friendsTuple.append('Ana')
print(friendsTuple)
