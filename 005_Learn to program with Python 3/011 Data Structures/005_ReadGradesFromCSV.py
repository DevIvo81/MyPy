# Read grades from *.csv file, compute grade letter for course

import os, csv  # Comma separated value package
os.system('cls')

DATA_FILE_NAME = 'GradesExample.csv'
POSSIBLE_POINTS = 200.
# Convert a number score to a letter grade:

def letterGrade(score):
    if score >= 90:
        letter = '5'
    elif score >= 80:
        letter = '4'
    elif score >= 70:
        letter = '3'
    elif score >= 60:
        letter = '2'
    else:
        letter = '1'  # fall through or default case
    return letter

# Open the file in 'read Universal'((return char) mode)
# This allows for dealing with files created by spreadsheet programs
# like Excel
fileHandle = open(DATA_FILE_NAME, 'r')

# Let the csv reader parse the file into rows
csvParsed = csv.reader(fileHandle)

# Treat each row (which represents data for single student) as a list
readingHeaderLine = True
for row in csvParsed:   # Iterate through each line
        
    if readingHeaderLine:   # first line?
        readingHeaderLine = False
        continue    # skip the header line

    # Data will look like: 
    # print(f'Original: {row}')

    name = row[0]   # save the student's name
    total = 0   # prepare to add them up
    for index in range(1,8):    # as elements 1-7 are scores
        thisGrade = row[index]
        if thisGrade == '':
            thisGrade = 0.0     # change noting to zero
        else:
            thisGrade = float(thisGrade)    # conversion to float
        total += thisGrade

    percent = (total*100.) / POSSIBLE_POINTS

    gradeToReport = letterGrade(percent)
    print(f'\n{name}\tPercent: {percent}\tGrade:{gradeToReport}')

print()

fileHandle.close()  # close the file