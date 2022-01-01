import os
os.system('cls')

# Adding game version 2

import random

score = 0

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
    