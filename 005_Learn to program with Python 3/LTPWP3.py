import os
os.system('cls')

### 5. LOOPS

######
# MadLib (version 5)

def chooseRandomFromList(aList):
    import random as r
    nItems = len(aList)
    randomIndex = r.randrange(0, nItems)
    randomElement = aList[randomIndex]
    return randomElement

namesList = ['Weird Al Yankovic', 'Teenage Mutant Ninja Turtles', 
             'Supergirl', 'Stay Puft Marshmallow Man', 
             'Shrek', 'Sherlock Holmes', 'The Beatles', 
             'Powerpuff Girl', 'Pillsburry Doughboy', 'Sam-I-Am']
verbsList = ['screamed', 'burped', 'ran', 'galumphed', 'rolled', 
             'ate', 'laughed', 'complained', 'whistled']
adjectivesList = ['purple', 'giant', 'lazy', 'curly-haired', 
                  'wireless electric', 'ten foot tall']
nounsList = ['ogre', 'dinosaur', 'Frisbee', 'robot', 'staple gun', 
             'hot dog vendor', 'tortoise', 'rodeo clown', 'unicorn', 'Santa hat', 'garbage can']

while True:
    name = chooseRandomFromList(namesList)
    verb = chooseRandomFromList(verbsList)
    adjective = chooseRandomFromList(adjectivesList)
    noun = chooseRandomFromList(nounsList)
    
    sentence = f'\n{name} {verb} through the forest, hoping to escape\nthe {adjective} {noun}!'
    print(sentence)
    
    if input('\n"q" to quit or anything else to continue: ').lower() == 'q':
        break
print('\nGOODBYE')



'''
######

print('\nTRY / EXCEPT')


print('\nGUESS THE NUMBER [1 --> 20]\n')

MAX_GUESSES = 5
MAX_RANGE = 20

def oneRound():
    
    target = random.randint(1, MAX_RANGE)

    guessCounter = 0

    while True:
        
        userGuess = input('\nTake a guess: ')
        try:
            userGuess = int(userGuess)
                
        except:
            print('\nThe number you entered is not an integer!')
            continue
        
        guessCounter += 1
        
        
        if userGuess == target:
            print(f'\nYou got it in {guessCounter} tries!')
            break
            
        elif userGuess < target:
            print('\nToo LOW!')
        else:
            print('\nToo HIGH!')

        if guessCounter == MAX_GUESSES:
            print(f'\nYou failed to guess in {MAX_GUESSES} tries!')
            print(f'\nThe number to guess was --> {target}')
            break
        

while True:
    oneRound()
    if input('\nPlay again? (ENTER to continue or "q" to quit) --> ').lower() == 'q':
        print('\nGOODBYE!')
        break

######

print('\nFLIPPING A COIN\n')

nFlips = 0
nHeads = 0
nTails = 0

maxFlips = int(input('\nHow many flips will be? --> '))
while nFlips < maxFlips:
    # heads or tails
    zeroOrOne = random.randint(0,1)
    if zeroOrOne == 0:
        nTails += 1
    else:
        nHeads += 1
    nFlips += 1

print(f'\nIn {maxFlips} flips we had {nTails} Tails and {nHeads} Heads')



###### 

print('\nRUNNING A PROGRAM MULTIPLE TIMES\n')

# Calculate total - repeated

def calcSum(target):
    
    total = 0
    nextNumToAddIn = 1

    while nextNumToAddIn <= target:
        # add in the next value
        total += nextNumToAddIn
        print(f'\nAdded in: {nextNumToAddIn}. Total so far is: {total}')
        # increment
        nextNumToAddIn += 1
    return total

answer = 'y'

while answer:
    userTarget = int(input('\nEnter a target number: '))
    thisTotal = calcSum(userTarget)
    print(f'\nThe sum of numbers from 1 to {userTarget} is --> {thisTotal}')
    
    answer = input('\nTry again? (Y or N): ').lower()


######

print('\nCALCULATING ARRAY SUM TO TARGET NUMBER\n')
target = int(input('\nEnter a target number: '))
total = 0
nextNumToAddIn = 1

while nextNumToAddIn <= target:
    total += nextNumToAddIn
    print(f'\nAdded in: {nextNumToAddIn}. Total so far is: {total}')
    nextNumToAddIn += 1

print(f'\nThe sum of numbers from 1 to {target} is --> {total}')



######

looping = True
while looping:
    answer = input('\nPlease type the letter "a": ').lower()
    if answer == 'a':
        looping = False
    else:
        print('\nCome on, type an "a"...')
print('\nTHANK YOU for an "a"!')

#######

### 4. USER DEFINED FUNCTIONS

######

# 4.5. CALCULATE SHIPPING

print(len('United States        Canada') * 2 * '-')
print('United States        \t\tCanada')
print(len('United States        Canada') * 2 * '-')
print(f'Quantity\tCost\t\tQuantity\tCost')
print(f'\n<= 50\t\t6.25\t\t<= 50\t\t8.25')
print(f'\n<= 100\t\t9.50\t\t<= 100\t\t12.50')
print(f'\n<= 150\t\t12.75\t\t<= 150\t\t18.75')
print(f'\nOtherwise\t15.00\t\tOtherwise\t25.00')

NOT_YET = "We don't ship there yet!"
def calcShip(country, nWidgets):
    
    if country == 'USA' or country == 'US' or country == 'UNITED STATES':
        if nWidgets < 50:
            shipCost = 6.25
        elif nWidgets < 100:
            shipCost = 9.50
        elif nWidgets < 150:
            shipCost = 12.75
        else:
            shipCost = 15.00
    
    elif country == 'CANADA' or country == 'CA':
        if nWidgets < 50:
            shipCost = 8.25
        elif nWidgets < 100:
            shipCost = 12.50
        elif nWidgets < 150:
            shipCost = 18.50
        else:
            shipCost = 25.00
    
    else:
        shipCost = NOT_YET
    
    return shipCost

userWidgets = int(input('\nEnter the number of widgets to ship --> '))
userCountry = input('\nEnter the country to ship to --> ').upper()

amountForShipping = calcShip(userCountry, userWidgets)

if amountForShipping == NOT_YET:
    print(f'\nSorry we do not ship to {userCountry} yet!')
else:
    print(f'\nIt will cost {amountForShipping}$ to ship to {userCountry}')    

######

# 4.4 isRectangle

def isRectangle(x, y):
    if x == y:
       return True
    else:
        return False

for i in range(6):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    if isRectangle(a, b):
        print(f'\nSides a = {a}  and b = {b} represent a SQUARE!')
    else:
        print(f'\nSides a = {a} and b = {b} represent a RECTANGLE!')


######

# 4.3. ISEVEN

def isEven(valueIn):
    if valueIn % 2 == 0:
        return True
    else:
        return False

def printEvenOrOdd(someValue):
    if isEven(someValue):
        print(f'\n{someValue} is EVEN!')
    else:
        print(f'\n{someValue} is ODD!')

x = [i for i in range(-15, 16, 1)]
x = tuple(x)
print(x)
print(type(x))

for i in x:
    printEvenOrOdd(i)


######

# 4.2 ISSQUARE

def isSquare(x, y):
    if x == y:
       return True
    else:
        return False

for i in range(6):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    if isSquare(a, b):
        print(f'\nSides a = {a}  and b = {b} represent a SQUARE!')
    else:
        print(f'\nSides a = {a} and b = {b} represent a RECTANGLE!')

# 4.1 NEG-POS-ZERO

def negativePositiveZero(x):
    if x < 0.0:
        answer = 'Negative'
    elif x > 0.0:
        answer = 'Positive'
    else:
        answer = 'Zero'
    return answer
    
r1es = negativePositiveZero(-22.4)
r2es = negativePositiveZero(25)
r3es = negativePositiveZero(0)

print(f'-22.4 is {r1es}, 25 is {r2es} and 0 is {r3es}')


######

def createHeader(fullName, gender):
    if gender == 'm':
        title = 'Mr.'
    elif gender == 'f':
        title = 'Ms.'
    else:
        title = 'Ms. or Mr.'
    header = f'Dear {title} {fullName}, '
    return header
print(createHeader('Ivo Ivic', 'm'))
print(createHeader('Ana Anic', 'f'))
print(createHeader('Pero Peric', 'm'))
print(createHeader('Vanja Vanjic', '?'))


######

def separateRuns():
    print('*' * 20)
    print(someUndefinedVariable)
    print()

def getGroceries(item1, item2, item3, item4):
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    separateRuns()

getGroceries('eggs', 'soap', 'lettuce', 'dry food')
getGroceries('beer', 'milk', 'soda', 'peas')



######

TAX_RATE = .09
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00

def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET + 
                nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost

total1 = calculateCost(4, 8)
print(f'\nTotal cost of the first order is {total1}')

total2 = calculateCost(12, 15)
print(f'\nTotal cost of the first order is {total2}')
    


######

def F2C(nDegreesF):
    nDegreesC = (nDegreesF - 32) * (5.0 / 9.0)
    return nDegreesC

def C2F(nDegreesC):
    nDegreesF = (nDegreesC * 1.8) + 32
    return nDegreesF

usersTempF = float(input('\nEnter a value of degrees Fahrenheit: '))
convertedTempC = F2C(usersTempF)
print(f'\n{usersTempF} °F is {round(convertedTempC)} °C')

usersTempC = float(input('\nEnter a value of degrees Celsius: '))
convertedTempF = C2F(usersTempC)
print(f'\n{usersTempC} °C is {round(convertedTempF)} °F')
print()
print(F2C(C2F(-18)))



######

def calculateAverage(param1, param2, param3, param4):
    
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    return average

yardsOnRun1 = 4
yardsOnRun2 = 6.5
yardsOnRun3 = 2.5
yardsOnRun4 = -2

averageYardsPerRun = calculateAverage(yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
print(f'\nAverage yards per run is {averageYardsPerRun}')

yardsOnPass1 = 0
yardsOnPass2 = 25.5
yardsOnPass3 = 0
yardsOnPass4 = 12

averageYardsPerPass = calculateAverage(yardsOnPass1, yardsOnPass2, yardsOnPass3, yardsOnPass4)
print(f'\nAverage yards per pass is {averageYardsPerPass}')

######

def square(number):
    answer = number * number
    return answer

def myFunction(p1arameter, p2arameter):
    a1nswer = square(p1arameter)
    a2nswer = square(p2arameter)
    a3nswer = square(p2arameter)
    return a1nswer, a2nswer, a3nswer
answers = myFunction(5, 10)

print(f'Answers are {answers}')

#######

def square(number):
    answer = number * number
    return answer
userNumber = float(input('\nEnter a number: '))
numberSquared = square(userNumber)
print(f'The number {userNumber} squared is {numberSquared}')


#######

def calculateAverage(param1, param2, param3, param4):
    
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    return average

a1Verage = calculateAverage(2, 3, 4, 5)
a2Verage = calculateAverage(-3, 5.2, 15, 1000.8)
a3Verage = calculateAverage(1.4, -2.5, 14.3, 200.5)

print(f'The average results are {a1Verage} {a2Verage} {a3Verage}')


######

def addTwo(startingValue):
    endingValue = startingValue + 2
    return endingValue

sum1 = addTwo(5)
sum2 = addTwo(10)
print(f'The results are 5 + 2 = {sum1}, 10 + 2 = {sum2}')

#######

def calculateAverage(param1, param2, param3, param4):
    
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    print(f'\nAverage value is {average}')

calculateAverage(2, 3, 4, 5)
calculateAverage(-3, 5.2, 15, 1000.8)
calculateAverage(1.4, -2.5, 14.3, 200.5)

######

def addTwo(startingValue):
    endingValue = startingValue + 2
    print(f'The sum of {startingValue} and 2 is: {endingValue}')

addTwo(5)
addTwo(10)

######

def separateRuns():
    print('*' * 20)
    print()

def getGroceries(item1, item2, item3, item4):
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    separateRuns()

getGroceries('eggs', 'soap', 'lettuce', 'dry food')
getGroceries('beer', 'milk', 'soda', 'peas')

mustGet = 'paper plates'
mustAlsoGet = 'chocolate candy bars'
getGroceries(mustGet, mustAlsoGet, 'lettuce', 'dryfood')

#######

def blend(setting, nMinutes):
       print(f'\nSetting is {setting} for {nMinutes} minutes')
desiredSetting = 'medium'
numberOfMinutes = 8
blend(desiredSetting, numberOfMinutes)

'''

