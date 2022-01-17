'''
What is an anagram? Well, two words are 
anagrams of each other if they both contain 
the same letters. 
For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the 
anagrams of a word from a list. You will 
be given two inputs a word and an array 
with words. You should return an array 
of all the anagrams or an empty array 
if there are none. 

For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

NOTE for Go
F
or Go: Empty string slice is expected when there are no anagrams found.
'''


import os
from random import randint as rnt
from random import choice as cc
os.system('cls')

def anagrams(word, words):
    
    anags = []
    
    for option in words:
        if sorted(list(set(option))) == sorted(list(set(word))):
            anags.append(option)
    
    return anags
    
    
    


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print()
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
print()
print(anagrams('laser', ['lazing', 'lazy', 'lacer']), [])
print()