'''
Check to see if a string has the 
same amount of 'x's and 'o's. The 
method must return a boolean and 
be case insensitive. The string 
can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is 
present should return true

XO("zzoo") => false
'''


import os
from random import randint as rnt
os.system('cls')

def is_prime(num):
    
    if num < 0:      
        num *= -1

    if num == 0 or num == 1:
        Flag = False

    else:
        for i in range(2, num):
            if num % i == 0:
                Flag = False
                break
            else:
                Flag = True
                break
        
        return Flag

number = rnt(-2**31, 2**31)

print(number)

print()

print(is_prime(number))

print()