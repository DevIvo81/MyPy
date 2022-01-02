"""FileReadWrite.py

Functions for checking if: 
    a file exists
    read from file 
    write to a file"""

import os


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
#
# Functions for opening a file, writing & reading a line at a time
# and closing the file

def openFileForWriting(filePath):
    fileHandle = open(filePath, 'w')
    return fileHandle

def writeALine(fileHandle, lineToWrite):
    # Add a new line character '\n' at the end and write the line
    lineToWrite += '\n'    
    fileHandle.write(lineToWrite)

def openFileForReading(filePath):
    if not fileExists(filePath):
        print(f'The file {filePath} does not exist - cannot read it')
        return ''
    fileHandle = open(filePath, 'r')
    return fileHandle

def readALine(fileHandle):
    theLine = fileHandle.readline()
    # This is a special check for attempting to read past the end of the
    # file (EOF)
    # If this occurs, let's return something unusual: False (which is not
    # a string)
    # If the caller wishes to check, their code can easily detect the end
    # of the file this way
    
    if not theLine:
        return False
    
    # If the line ends with a newline character '\n', then strip that off
    # the end
    
    if theLine.endswith('\n'):
        theLine = theLine.rstrip('\n')
    
    return theLine

def closeFile(fileHandle):
    fileHandle.close()
