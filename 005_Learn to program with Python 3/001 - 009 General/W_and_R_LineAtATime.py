# WRITING AN READING A LINE AT A TIME WITH FILE
import os
os.system('cls')

# WRITE IN MULTPLE LINES DATA IN FILE

from FileReadWrite import *

DATA_FILE_PATH = 'MultiLineData.txt'

myFileHandle = openFileForWriting(DATA_FILE_PATH)

data1 = 'Here is some data as a string'
writeALine(myFileHandle, data1)
data2 = 'Here is a second line of string data'
writeALine(myFileHandle, data2)

# Could have some code join several pieces of data into a
# single string
data3 = '123,Ivo Zelic,123.45,0'
writeALine(myFileHandle, data3)

closeFile(myFileHandle)

# READ MULTPLE LINES DATA FROM FILE

myFileHandle = openFileForReading(DATA_FILE_PATH)

data1 = readALine(myFileHandle)
print(data1)
data2 = readALine(myFileHandle)
print(data1)
data3 = readALine(myFileHandle)
print(data3)

closeFile(myFileHandle)
