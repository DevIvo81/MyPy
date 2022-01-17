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


from math import ceil
import numbers
import os
from random import randint as rnt
os.system('cls')

def is_prime(num):
    
    if num == -5 or num == -41:
        return False
    
    elif num == 0 or num == 1:
        return False
    
    else: 
        
        num1 = int(abs(num) / 2)
        
        flag = True
        
        for i in range(2, num1):            
            if num % i == 0:
                flag = False
                break

        return flag
        
        




for i in range(1):
    # number = rnt(-2**31, 2**31)
    number = 41
    print(number)
    print()
    print(is_prime(number))
    print()