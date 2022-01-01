import os
os.system('cls')

# Increment test
from FileReadWrite import *
# File name as CONSTANT
DATA_FILE_PATH = 'CountData.txt'

# Main program - reads from file, increments a counter, writes to file

if not fileExists(DATA_FILE_PATH):
    # The file was not found as this is a first time
    # we run the program
    print('\nFirst time - creating the data file.\n') # for testing
    writeFile(DATA_FILE_PATH, '1')
else:
    # The file was found. We have run this program before
    count = int(readFile(DATA_FILE_PATH))
    count += 1
    print(f'\nFound te file, data read was {count}')
    textToWrite = str(count)
    writeFile(DATA_FILE_PATH, textToWrite)
    print(f'\nThis was run number: {count}\n')
    