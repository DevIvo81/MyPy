import os, random, locale, string
os.system('cls')
# locale.setlocale(locale.LC_ALL, 'hrv')
# print(locale.getlocale())


# EXCERCISE 1

'''name = input('\nName: ')
yob = int(input('\nHow old are you: '))

print(f'Hey, {name}... You will get 100 years old at {2021- yob + 100}')

num = int(input('\nInput number: '))
check = int(input('\nInput number to divide by: '))'''

# EXCERCISE 2

'''if num % check == 0:
    print(f'\nNumber {num} divides by {check} evenly!')
else:
    print(f'\nNumber {num} NOT divide by {check} evenly!')

if num % 4 == 0:
    print('\nNumber is a multiple of 4!')
elif num % 2 == 0:
    print('\nNumber is even!')
else:
    print('\nNumber is odd!')'''

# EXCERCISE 3

'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = int(input('\nInput number for reference: '))
b = [i for i in a if i < c]


print(f'\nOriginal list: {a}')

print(f'\nNumbers less than {c} are {b}')'''


# EXCERCISE 4

'''num = int(input('Input number: '))
print([x for x in range(1, num) if num % x == 0])'''


# EXCERCISE 5

'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f'\nList a = {a}')
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f'\nList b = {b}')

common = []

for i in a:
    for j in b:
        if j not in common and j == i:
            common.append(j)        
print(f'\nList of common elements = {common}')

common = []

a = [random.randint(1, 99) for i in range(11)]
print(f'\nRandom List a = {a}')
b = [random.randint(1, 99) for i in range(13)]
print(f'\nRandom List b = {b}')


for i in a:
    for j in b:
        if j not in common and j == i:
            common.append(j)
print(f'\nList of common random elements = {common}')'''

# EXCERCISE 6

'''print('\nPALINDROME CHECK!')

# all input letters upper
sentence = input('\nInput sentence: ').upper()

# sentence list without blanks
orig_list = [i for i in sentence if i != ' ']
print(orig_list)

# reverse list
orig_list.reverse()

# reversed list as a new variable
back_list = orig_list 

# original list return
orig_list = [i for i in sentence if i != ' ']

print()
print(back_list)

if orig_list == back_list:
    print('\nPALINDROME!!')
else:
    print('\nNOT palindrome...!')'''

# EXCERCISE 7

'''a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f'\nOriginal list {a}')
print(f'\nList with even numbers {[i for i in a if i % 2 == 0]}')'''

# EXCERCISE 8

'''while True:
    
    a = input('\n1. player - input ["R", "P" or "S"]: ').lower()
    os.system('cls')
    b = input('\n2. player - input ["R", "P" or "S"]: ').lower()

    if b == a:
        print("\nDraw!")
    elif a == 'r' and b == 'p':
        print('\n2.p wins!')
    elif b == 'r' and a == 'p':
        print('\n1.p wins!')

    elif a == 'p' and b == 's':
        print('\n2.p wins!')
    elif b == 'p' and a == 's':
        print('\n1.p wins!')

    elif a == 's' and b == 'r':
        print('\n2.p wins!')
    elif b == 's' and a == 'r':
        print('\n1.p wins!')
    
    if input('\nPLAY AGAIN [Y/N]: ').upper() == 'N':
        print('\nGOODBYE!')
        break
'''

# EXCERCISE 9

'''
n = random.randint(1, 9)

tries = 1

while True:
      
    a = int(input('\nInput number: '))
    
    if a == n:
        print(f"\nThe number {a} is the correct number! in {tries} tries!")
        break

    else:
        if a > n:
            print('\nLower than that!')
            tries += 1
        else:
            print('\nHigher than that!')
            tries += 1
'''

# EXCERCISE 10

'''
a = random.sample(range(1,30), 12)
print(f'\nList a = {a}')

b = random.sample(range(1,30), 16)
print(f'\nList b = {b}')

common = [j for i in set(a) for j in set(b) if j == i]
print(f'\nCommon elements list = {common}')
'''

# EXCERCISE 11

'''
def prime_check(x):
    for i in range(2, x):
        if x % i == 0:
            return print(f'\nNumber {x} IS NOT a prime number!')
        else:
            return print(f'\nNumber {x} is a PRIME number!')

while True:
    
    x = input('\nInput number: ')

    if x.isdigit() == False:
        print(f'\nInput {x} contains letters! Try again.')
    
    else:
        x = int(x)
        prime_check(x)
    
        if input('\nTRY AGAIN [Y/N]: ').upper() == 'N':
            print('\nGOODBYE!')
            break
'''

# EXCERCISE 12

'''
def first_and_last(a):
    b = [a[0], a[len(a)-1]]
    return print(f'\nList of the first and last element -> {b}')

a = [random.randint(1,30) for i in range(6)]
print(f'\nOriginal list -> {a}')

first_and_last(a)
'''

# EXCERCISE 13

'''
def fibonacci(x):
        
    i = 1

    if x == 0:
        fibo_list = []
    elif x == 1:
        fibo_list = [1]
    elif x == 2:
        fibo_list = [1, 1]
    else:
        fibo_list = [1, 1]
        while i < x-1:
            fibo_list.append(fibo_list[i] + fibo_list[i-1])
            i += 1
    return print(fibo_list)


while True:

    x = input('\nInput Fibonacci array length: ')
    
    if x.isdigit() == False:
        print(f'\nInput {x} contains letters! Try again.')
    
    else:
        x = int(x)

        fibonacci(x)

        
        if input('\nTRY AGAIN [Y/N]: ').upper() == 'N':
            print('\nGOODBYE!')
            break
'''

# EXCERCISE 14
'''
def construct():
        
        x = input('\nInput number of elements: ')
        
        if x.isdigit() == False:
            print(f'\nThe input {x} contains letters! Try again!')
        
        else:
            x = int(x)
            b = []
            a = [random.randint(1, 99) for i in range(x)]
            print(f'\nOriginal list ->\t{a}')
            for i in a:
                if i not in b:
                    b.append(i)
            return print(f'\nNo duplicates list ->\t{b}')

construct()
'''

# EXCERCISE 15
'''
s = input('\nInput Sentence: ')
print()
print(s)


def rev_string(s):
    s = s.split()
    s = s[::-1]
    s = ' '.join(s)
    return print(s)

print()
rev_string(s)
'''

# EXCERCISE 16
'''
def strongPass():
    
    password = ''
    
    up_Chr = 'ABCDEFGHIJKLMMNOPQRSTUVWXYZ'
    lo_Chr = 'abcdefghijklnopqrstuvwxyz'
    spc_Chr = '!#$%&/()=?+*-_[{]}'
    num_Chr = '1234567890'

    password += random.choice(num_Chr)
    password += random.choice(lo_Chr)
    password += random.choice(spc_Chr)
    password += random.choice(up_Chr)
    password += random.choice(num_Chr)
    password += random.choice(lo_Chr)
    password += random.choice(spc_Chr)
    password += random.choice(up_Chr)

    return password

def weakPass():

    password = ''

    up_Chr = 'ABCDEFGHIJKLMMNOPQRSTUVWXYZ'
    
    lo_Chr = 'abcdefghijklnopqrstuvwxyz'
    
    num_Chr = '1234567890'

    password += random.choice(num_Chr)
    password += random.choice(lo_Chr)
    password += random.choice(up_Chr)
    password += random.choice(num_Chr)
    password += random.choice(lo_Chr)
    password += random.choice(up_Chr)

    return password



question = input('\nWhat kind of password Strong or Weak [S or W]: ')
question = question.upper()

strong = strongPass()
weak = weakPass()

if question == 'S':
    print(f'\nStrong password --> {strong}')
elif question == 'W':
    print(f'\nWeak password --> {weak}')
'''

# EXCERCISE 17

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())