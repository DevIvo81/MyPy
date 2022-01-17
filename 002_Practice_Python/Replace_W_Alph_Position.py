'''
In this kata you are required to, 
given a string, replace every letter 
with its position in the alphabet.

If anything in the text isn't a letter, 
ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 
20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

'''

import os
from random import randint as rnt
os.system('cls')

def alphabet_position(text):
    
    import string
    
    alphaDict = {c : (i + 1) for i, c in enumerate(string.ascii_lowercase)}
   
    for char in text:
        if char == ' ' or char in (string.punctuation + "'"):
            text = text.replace(char, '')
    
    textList = list(text.lower())
            
    newList = [str(alphaDict[char]) for char in textList]

    return ' '.join(newList)
    

print(alphabet_position("C'mon Elden's Ring!"))
    
    


