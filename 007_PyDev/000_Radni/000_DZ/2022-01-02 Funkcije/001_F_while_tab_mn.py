# 1. TABLICA MNOŽENJA
import os, random
os.system('cls')

def ispisTabliceMnoženja(n):
    for redak in range(1, n + 1):
        
        for stupac in range(1, n + 1):
            if len(str(redak*stupac)) == 1:
                print(f'   {redak*stupac} ', end='')
            elif len(str(redak*stupac)) == 2:
                print(f'  {redak*stupac} ', end='')
            elif len(str(redak*stupac)) == 3:
                print(f' {redak*stupac} ', end='')  
            else:
                print(f'{redak*stupac} ', end='')
        print()

 
while True:
        
    RASPON = input('\nUpiši broj do kojeg množimo: ')
    
    print()
    
    if RASPON.isdigit() == False:
        print('\nBrojevi se traže, ne slova! Pokušaj ponovno!')
    
    else:
        RASPON = int(RASPON)
        ispisTabliceMnoženja(RASPON)
        
        if input('\nŽelite li pokušati ponovno ("n" za izlaz) --> ').lower() == 'n':
            print()
            print('\nDo sljedećeg puta, pozdrav!\n')
            break