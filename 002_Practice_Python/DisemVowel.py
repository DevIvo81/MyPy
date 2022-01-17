import os
os.system('cls')



def disemvowel(string_):
    
    vowels = ['a', 'e', 'i', 'o', 'u',
              'A', 'E', 'I', 'O', 'U', 
              '0']
    
    for char in vowels:
        if char in string_:
            string_ = string_.replace(char, '')
    
    return string_

spam = 'This website is for losers, LOL!'

print(disemvowel(spam))