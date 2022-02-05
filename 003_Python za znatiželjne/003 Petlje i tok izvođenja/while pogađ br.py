import os
from random import randint as rnt

os.system('cls' if os.name =='nt' else 'clear')

#region POGAĐANJE BROJEVA

"""
print('''
    --------------------------------
    | POGAĐAMO BROJ IZMEĐU 1 I 100 |
    --------------------------------
    ''')

broj_koji_pogadamo = rnt(1, 99)
broj_pokusaja = 1

while True:
    unos = input('\nUpiši broj --> ')
    if not unos.isdigit():
        print('\nBROJ SE TRAŽI!')
        continue

    unos = int(unos)
    
    if unos < broj_koji_pogadamo:
        print('\nVEĆI je od toga!')
        broj_pokusaja += 1
        continue
    
    elif unos > broj_koji_pogadamo:
        print('\nmanji je od toga!')
        broj_pokusaja += 1
        continue
    
    else:
        print(f'\nBRAVO, POGODAK u {broj_pokusaja} pokušaja!\n')
        break
"""

#endregion


#region ZADACI
print('\nPRVA PETLJA\n')
broj = 100
while broj >= 0:
    broj -= 1
    if broj % 3 != 0:
        continue
    print(broj, end=', ')
        

print('\n\nDRUGA PETLJA\n')
broj = 100
while broj >= 0:
    broj -= 1
    if broj % 3 == 0:
        print(broj, end=', ')
        
        
print('\n\nTRETJA PETLJA\n')

for broj in range(11):
    if broj % 2 == 0:
        continue
    if broj % 5 == 0:
        break
    print(broj, end=' ')