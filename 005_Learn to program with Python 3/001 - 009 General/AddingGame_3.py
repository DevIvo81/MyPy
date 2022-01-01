import os
os.system('cls')

# Adding game version 3
# Save only the score

import random
from FileReadWrite import *

# File with path as a CONSTANT
DATA_FILE_PATH = 'GameData.txt'

# Start up code
if not fileExists(DATA_FILE_PATH):
    score = 0
    print('\nHello, welcome to the Adding game!\n')

else:
    score = int(readFile(DATA_FILE_PATH))
    print(f'\nWelcome back! Your score is {score}\n')

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
    
    if userAnswer == correctAnswer:
        score += 2
        print('\nThat is correct!')
        
    else:
        print(f'\nNo... The correct userAnswer was: {correctAnswer}')
        score -= 1
    print(f'\nYour current score is --> {score}\n')

writeFile(DATA_FILE_PATH, str(score))
print('\nThanks for playing!\n')
       