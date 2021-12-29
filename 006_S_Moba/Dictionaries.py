import os, random, string
os.system('cls')

# 7. REMOVE GIVEN KEY FROM DICTIONARY

d = {'A' : 46, 'B' : 32, 'C' : 22, 'D' : 87, 'E' : 65, 'F' : 71}

print(f'Before pop("A")\n\n\t{d}')
d.pop('A')

print(f'\nAfter pop("A")\n\n\t{d}')

'''

# 6. MULTIPLICATION OF DICTIONARY VALUES

d = {'A' : 46, 'B' : 32, 'C' : 22}
multi = 1
for i in d.values():
    multi *= i
print(f'The multiplication of dictionary values is {multi}')

# 5. SUM OF DICTIONARY VALUES

d = {'A' : 46, 'B' : 32, 'C' : 22}
suma = 0
for i in d.values():
    suma += i
print(f'The sum of dictionary values is {suma}')

# 4. DICTIONARY {x : x * x}

print({x : x**2 for x in range(1,21)})


# 3. CHECK IF KEY EXISTS

dct = { str(i) : string.ascii_uppercase[i] for i in range(10) }
print(dct)

key = input('\nEnter key to search for: ')

if key in dct:
    print(f'\nThe key {key} exists in dictionary. It is {dct[key]}')
else:
    print(f'\nThe key {key} is not in dictionary.')



# 2. CONCATENATE 2 DICTIONARIES IN 1

fDct = {string.ascii_uppercase[i] : i for i in range(0, 3)}
sDct = {string.ascii_uppercase[i] : i for i in range(4, 6)}

print(f'First dictionary -->\t{fDct}'
      f'\n\nSecond dictionary -->\t{sDct}')
fDct.update(sDct)
print(f'\nConcatenated ditionaries-->\t{fDct}')

# 1. CREATE A DICTIONARY KEY:VALUE

dct = {string.ascii_uppercase[i] : i for i in range(10)}
print(dct)
'''