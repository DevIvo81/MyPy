# 1. TABLICA MNOŽENJA
import os, random
os.system('cls')

os.system('cls')

#n = int(input('\nUpiši broj do kojeg množimo: '))
n = 8
print('\nIspisujemo tablicu množenja\n')

while True:
    print()
    for redak in range(1, n + 1):
        for stupac in range(1, n + 1):
            print(f'{redak}x{stupac}={redak*stupac}', end='\t')
        print()
        
    if input('\nŽelite li pokušati ponovno (N za prekid) --> ').upper() == 'N':
            print()
            print('\n Do sljedećeg puta, pozdrav!\n')
            break