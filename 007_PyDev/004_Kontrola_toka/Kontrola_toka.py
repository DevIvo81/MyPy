'''
A       B       A and B    A or B
True    True    True        True
True    False   False       True
False   True    False       True
False   False   False       False
'''

'''
# prvi_uvjet = True
# drugi_uvjet = False
# treći_uvjet = True

lista = [i for i in range(1, 31) if ]

for broj in brojevi:
    if broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 3.')
    elif broj % 6 == 0:
        print(f'Broj {broj} je djeljiv s 6.')
    elif broj % 9 == 0:
        print(f'Broj {broj} je djeljiv s 9.')
    else:
        print(f'Broj {broj} nije djeljiv s 3, 6 i 9.')
    '''

'''
rijec = input('\nUpiši neku riječ: ')
rijec = rijec.upper()
pal = rijec[ : : -1]
if rijec == rijec[ : : -1]:
    print(f'\nRijec {rijec} je palindrom!')
else:
    print(f'\nRijec {rijec} nije palindrom!')
'''  

'''
"Unos znaka i broj ponavljanja znaka"
M-M-M-M-M
'''

# znak = input('\nUpiši znak: ')
# pon = int(input('\nUpiši broj ponavljanja: '))

# lista = []
# for i in range(pon):
#     lista.append(znak)

# print('\nIspis ', end='')
# print(*lista, sep='-')
# print()

'''
A = 7

******* *******
 ****** ******
  ***** *****
   **** ****
    *** ***
     ** **
      * *
'''

import os


while True:
    
    os.system('cls')
    
    a = 'BOR S RAZMAKOM U SREDINI NAOPAKO!'
    print()
    print(a)
    print('_' * len(a) + '\n')
    
    zvijezde = int(input('\nUnesi početni broj * '))
    print()
       
    brojac = 0

    for i in range(zvijezde, 0, -1):
        print('*' * i + ' ' + '*' * i, end='\n')
        brojac += 1
        print(' ' * brojac, end='')
    
    # BOR S RAZMAKOM U SREDINI

    b = 'BOR S RAZMAKOM U SREDINI!'
    print()
    print()

    print(b)
    print('_' * len(b))


    zvjezdice = int(input('\nUnesi konačni broj * '))

    print()

    cajger = zvjezdice

    for j in range(zvjezdice):
            cajger = zvjezdice - j
            print(' ' * cajger, end='')
            print('*' * j + ' ' + '*' * j, end='\n')
            cajger -= 1
            
    if input('\nJoš jednom [Y / N]?  ').lower() =='n':
        print('\nDo sljedećeg puta, pozdrav!')
        break
    
