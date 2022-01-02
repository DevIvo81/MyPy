import os
os.system('cls')

programmingDict = {\
    'variable' : 'A named memory location that holds a value', 
    'loop' : 'A block of code that is repeated until a certain condition is met',
    'function' : 'A series of related steps that form a larger task, \noften called from multiple places in a program', 
    'constant' : 'A variable whose value does not change',
    'Boolean' : 'A data type that can only have values of True or False'}

while True:
    
    usersWord = input('\nEnter a word to look up  (or press ENTER to exit): ')
    
    if usersWord == '':
        print('\nFarewell!\n')
        break
    if usersWord in programmingDict:
        print(f'\n{programmingDict[usersWord]}')
    else:
        print(f'\nSorry, no data for {usersWord}')
        yesOrNo = input(f'\nWould you like to add a definition for {usersWord} (Yes/No): ')
        if yesOrNo.lower() == 'y':
            usersDefinition = input(f'\nPlease type a definition for {usersWord}: ').capitalize()
            programmingDict[usersWord] = usersDefinition
            print('\Thanks, got it!')
