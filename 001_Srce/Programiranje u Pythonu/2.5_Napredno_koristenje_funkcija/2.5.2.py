'''2.  Napišite program koji će s tipkovnice učitati jednu 
proizvoljnu cjelobrojnu vrijednost. Za tako učitani cijeli 
broj prebrojite i ispišite koliko se parnih znamenki nalazi 
u njemu. Prebrojavanje parnih znamenki napravite pomoću 
rekurzivne funkcije. Na primjer, za broj 12345, 
potrebno je na zaslon ispisati vrijednost 2.'''
import os
os.system('cls')

def parne_znamenke(x):
    
    if x == 0:
        return 0
    elif x % 2 == 0:
        return 1 + parne_znamenke(x // 10)
    else:
        return parne_znamenke(x // 10)

x = input('\nUpiši cijeli višeznamenkasti broj: ')
x = int(x)

broj = parne_znamenke(x)
print(f'\nU broju {x} ima {broj} parnih znamenki')


