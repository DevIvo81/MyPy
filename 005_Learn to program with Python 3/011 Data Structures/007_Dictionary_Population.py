import os
os.system('cls')

# Get the population of a given state

statesDict = {\
    'California' : 39776830, 'Texas' : 28704330, 'Florida' : 2131221, \
        'New York' : 19862512, 'Pennsylvania' : 12823989, 'Illinois' : 12768320, \
            'Ohio' : 11694664, 'Georgia' : 10545138, 'North Carolina' : 10390149, \
                'Michigan' : 9991177, 'New Jersey' : 9032872, 'Virginia' : 8525660,\
                    }

# for state in statesDict:
#     print(state)

for state in statesDict:
    population = statesDict[state]
    print(f'\n{state} population is {population}')

# while True:
#     userState = input('\nPlease enter a state name (or press ENTER to exit): ').title()
#     if userState == '':
#         print('\nFarewell!\n')        
#         break
#     if userState in statesDict:
#         print(f'\nThe population of {userState} is {statesDict[userState]}')
#     else:
#         print(f'\nSorry, there is no information on {userState}.')
#     print()


        
