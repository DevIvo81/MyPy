'''
Write a method that takes an array of 
consecutive (increasing) letters as input 
and that returns the missing letter in the 
array.

You will always get an valid array. And it 
will be always exactly one letter be missing.
The length of the array will always be at 
least 2.
The array will always contain letters in only 
one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"

NOTE Use the English alphabet with 26 letters!
'''

import os
from random import randint as rnt
from random import choice as cc
os.system('cls')

def find_missing_letter(chars):
    import string
    
    lowAndUpp = list(string.ascii_lowercase + string.ascii_uppercase)
           
    charSlice = lowAndUpp[lowAndUpp.index(chars[0]) : lowAndUpp.index(chars[-1]) + 1]
    
    for char in chars:
        if char in charSlice:
            charSlice.remove(char)
    
    return charSlice[0]
    
    
    
print(find_missing_letter(['a','b','c','d','f']), 'e')
print()
print(find_missing_letter(['O','Q','R','S']), 'P')
print()