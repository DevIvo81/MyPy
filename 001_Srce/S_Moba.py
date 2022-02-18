#### CONDITIONAL STATEMENTS ####
import os, random, string
os.system('cls')

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)
# print(string.printable)

# 15. NUMBERS [100 - 400] WITH EVEN DIGITS

even_list = []

for i in range(100, 401):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0:
        even_list.append(i)
    
print(*even_list, sep=', ')


'''
# 14. PASSWORD VALIDITY

print(f'\nTerms for password validity:', 
      f'\n\n\t- Length between 6 and 16 characters',
      f'\n\t- At least one UPPER and one lower letter',
      f'\n\t- At least one number [0-9]',
      f'\n\t- At least one upper and one lower letter',
      f'\n\t- At least one character from {string.punctuation}')

pword = input('\nEnter password: ')

upp_char = string.ascii_uppercase
low_char = string.ascii_lowercase
numbers = string.digits
specials = string.punctuation

check = []
    
for c in pword:
    if c.isupper():
        check.append(1)
    elif c.islower():
        check.append(2)     
    elif c.isdigit():
        check.append(3)
    elif c in specials:
        check.append(4)


if 6 <= len(pword) <= 16:
    check.append(5)
check = set(check)
print(check)
if len(check) == 5:
    print(f'\nPassword {pword} is VALID')
else:
    print(f'\nPassword {pword} is NOT VALID')
'''


'''
# 13. NUMBER OF LETTERS AND DIGITS IN STRING

my_string = input('\nEnter string of numbers and letters: ')

nums = 0
lets = 0

for i in my_string:
    if i.isdigit() == True:
        nums += 1
    else:
        lets += 1
print(f'The string {my_string} contains {lets} letters and {nums} numbers.')

'''
'''    
# 11. BLANK LINE TO TERMINATE

lines = []

while True:
    l = input('\nBlank line terminates ')
    if l:
        lines.append(l.upper())
        print(*lines, end=' ')
    else:
        break
    
# for l in lines: 
#     print(l)
'''

'''
# 9. Fizz & Buzz

integers = [i for i in range(1, 51)]

for i in range(len(integers)):
    if integers[i] % 3 == 0 and integers[i] % 5 == 0:
        integers[i] = 'FizzBuzz'
    elif integers[i] % 3 == 0:
        integers[i] = 'Fizz'
    elif integers[i] % 5 == 0:
        integers[i] = 'Buzz'

print('\nFizz & Buzz: ',integers)
    
'''    


'''
# 8. FIBONACCI SERIES BETWEEN 0 TO 50

x, y = 0, 1

while y < 50:
    print(y, end=' ')
    x, y = y, x + y
'''    

'''
# NUMBERS [0, 6] WITHOUT 3 AND 6

print()
lista = [i for i in range (7) if not i == 3 and not i == 6]
print(*lista, sep = ' ')
print()
'''

'''
# PRINT TYPE OF ITEMS IN LIST

lista = [5223, 54.88, 1+2j, True, 'programiranje', 
         (-1, -2), [6, 18], {'row': 'R', 'col' : 'C'}]

for i in lista:
    print(f'\nType of {i} is {type(i)}')
'''


'''
# COUNT NUMBER OF EVEN AND ODD NUMBERS FROM SERIES OF NUMBERS

series = [random.randint(1,1000) for i in range(101)]
print(f'\n-- Series of numbers -- \n\n{series}')
even = 0
odd = 0

for i in series:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'\nIn upper series of numbers there are {even} even and {odd} odd numbers.')
'''
'''
# 1 <= n <= 9 , guess number between

correct = random.randint(1, 9)

print(correct)

print('\nTry to guess a number between 1 and 9')

tries = 0
lista = []

while True:
    n = input('\nEnter the number: ')
    if n.isdigit() == False:
        print('\nNUMBERS NOT LETTERS!')
    else:
        n = int(n)
        
        if n < 1 or n > 9:
           print('\nOUT OF RANGE!') 
        
        elif n > correct:
            tries += 1
            lista.append(n)
            print('\nLower than that!')
        
        elif n < correct:
            tries += 1
            lista.append(n)
            print('\nHIGHER than that!')
        
        else:
            tries += 1
            lista.append(n)
            print(f'\nCORRECT! You guessed it in {tries} tries!\n\nYou tried numbers {lista}')
            break
'''

'''
# 1500 <= n <=2700 , n divisible by 7 and 5

lista = [n for n in range(1500, 2700 + 1) 
         if n % 5 == 0 and n % 7 == 0]

print(f'Requested numbers are {lista}')
'''                        