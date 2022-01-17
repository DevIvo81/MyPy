'''
A Narcissistic Number is a positive 
number which is the sum of its own 
digits, each raised to the power of 
the number of digits in a given base.

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
'''

import os
from random import randint as rnt
os.system('cls')

def narcissistic(value):
    
    valDigitList = []
    val = value
    
    while val > 0:
        broj = val % 10
        valDigitList.append(broj)
        val //= 10
    
    narc = 0
    
    for i in valDigitList:
        narc += i ** (len(valDigitList))
        
    if narc == value:
        return True
    else:
        return False



print(narcissistic(9474))

for i in range(1, 1000001):
    if narcissistic(i):
        print(i)
