import os
os.system('cls')

# Adding game version 1

import random

firstNumber = random.randrange(0, 11)
secondNumber = random.randrange(0, 11)
correctAnswer = firstNumber + secondNumber

question = f'\nHow much is {firstNumber} + {secondNumber} = '
userAnswer = int(input(question))

if userAnswer == correctAnswer:
    print('\nThat is correct!')
else:
    print(f'\nNo... The correct userAnswer was: {correctuserAnswer}')
print()