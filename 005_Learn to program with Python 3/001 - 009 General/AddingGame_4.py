import os
os.system('cls')


# myList = ['abc', 'de', '123', 'fghi', '-3.21']
# myString = ', '.join(myList)
# print(myString)
# myList = myString.split(', ')
# print(myList)


# Adding game version 4

import random
from FileReadWrite import *

# File with path as a CONSTANT
DATA_FILE_PATH = 'AddingGameData.txt'

# Main program starts here

if not fileExists(DATA_FILE_PATH):
    print('\nHello, welcome to the Adding game!')
    userName = input('\nYou must be new here, please enter your name: ')
    score = 0
    nProblems = 0
    nCorrect = 0
    
    print('\nTo quit the game press ENTER and your info will be saved.')
    print(f"\nOK, {userName}, let's get started...\n")

else:
    savedDataString = readFile(DATA_FILE_PATH) # read he whole variable
    savedDataList = savedDataString.split(', ')
    userName = savedDataList[0]
    score = int(savedDataList[1])
    nProblems = int(savedDataList[2])
    nCorrect = int(savedDataList[3])
    print(f'\nWelcome back, {userName} Your current score is {score}\n')

# Main Loop

while True:
    firstNumber = random.randrange(0, 11)
    secondNumber = random.randrange(0, 11)
    correctAnswer = firstNumber + secondNumber

    question = (f'\nENTER exits the program \
                  \n\nHow much is {firstNumber} + {secondNumber} = ')
    
    userAnswer = input(question)
    
    if userAnswer == '':
        print(f'\nFarewell, your score is {score}\n')
        break
    
    userAnswer = int(userAnswer)
    nProblems += 1
    
    if userAnswer == correctAnswer:
        print('\nThat is correct!')
        score += 2
        nCorrect += 1
    else:
        print(f'\nNo... The correct userAnswer was: {correctAnswer}')
        score -= 1
    print(f'\nYour current score is --> {score}\n')

writeFile(DATA_FILE_PATH, str(score))
print('\nThanks for playing!\n')
print(f'\nYou have tried {nProblems} problems and correctly answered {nCorrect}\n')

# Make a list of username, score, nProblems, nCorrect then
# create string from list using join
dataList = [userName, str(score), str(nProblems), str(nCorrect)]
outputText = ', '.join(dataList)

writeFile(DATA_FILE_PATH, outputText)


