'''
You will be given a number and you 
will need to return it as a string 
in Expanded Form. 
For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.



'''

import os
from random import randint as rnt
os.system('cls')

def expanded_form(num):
    
    expanded = []
    
    while num > 0:
        broj = num % 10
        expanded.append(broj)
        num //= 10
    
    express = [f'{expanded[i]}{"0" * i}' for i in range(len(expanded)) if int(expanded[i]) != 0]    
    
    express = express[ : : -1]
    
    form = ' + '.join(express) 
    
    return form

print(expanded_form(40232))





