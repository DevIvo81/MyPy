# FileReadWrite CODE

import os
os.system('cls')

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filePath):
    if not fileExists(filePath):
        print(f'\nThe file {filePath} does not exist - cannot read it.')
        return ''
    
    else:
        fileHandle = open(filePath, 'r')
        data = fileHandle.read()
        fileHandle.close()
        return data

# path to the file as CONSTANT
DATA_FILE_PATH = r'TestData.txt'
# DATA_FILE_PATH = 'C:/Users/Nafta/Desktop/MyPy/005_Learn to program with Python 3/TestData.txt'

stringToWriteOutToFile = 'ABCDEFGHIJKL' # any contens
writeFile(DATA_FILE_PATH, stringToWriteOutToFile) # call a write function

stringReadInFromFile = readFile(DATA_FILE_PATH)
print(f'\nRead in: {stringReadInFromFile}')


