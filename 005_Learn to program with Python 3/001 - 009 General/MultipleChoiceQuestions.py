import os
os.system('cls')

# MULTIPLE CHOICE TEST

import random
from FileReadWrite import *

FILE_PATH = 'MultipleChoiceQuestions.txt'
LETTERS_LIST = [a, b, c, d]

# Open the file for reading, read in the title line
fileHandle = openFileForReading(FILE_PATH)
titleText = readALine(fileHandle)

# Find out how many questions will be
nQuestions = int(readALine(fileHandle))

print('\nWelcome! This test is:\n')
print(titleText) # print whatever title we got from file
print(f'\nThere will be {nQuestions} questions.')
print("\nLet's go...\n")




