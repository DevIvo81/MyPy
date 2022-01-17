'''
Complete the function scramble(str1, str2) 
that returns true if a portion of str1 
characters can be rearranged to match str2, 
otherwise returns false.

Notes:

Only lower case letters will be used (a-z). 
No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

import os
from random import randint as rnt
from random import choice as cc
os.system('cls')

def scramble(s1, s2):
    
    s1 = set(s1)
       
    s2 = set(s2)
    
    counter = 0       
    
    for char in s2:
        if char in s1:
            counter += 1
    return True if counter == len(s2) else False
        
print(scramble('muthmahqacykvyk', 'ivwucciapdfvftdi'),  False)
print(scramble('vohievjqpzypfkvfpm', 'cnooakaeufuh'),  False)
print(scramble('rkqodlw', 'world'),  True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)