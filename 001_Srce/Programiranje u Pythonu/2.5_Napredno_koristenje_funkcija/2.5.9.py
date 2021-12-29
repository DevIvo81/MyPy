'''9.  * Napišite program koji će s tipkovnice učitati jednu 
proizvoljnu cjelobrojnu vrijednosti. Za tako učitani broj, 
odredite pomoću rekurzivne funkcije je li on prost broj. 
Ako je učitani broj prost, ispišite na zaslon poruku: "Prost je!", 
u suprotnom ispišite "Nije prost!".'''
import os
os.system('cls')

def daLiJeProst(x):
    def pretraga(x, i):
        if x == i:
            return True
        if x % i == 0:
            return False
        return pretraga(x, i + 1)
    return pretraga(x, 2)

x = input('Upiši cijeli broj: ')
x = int(x)

if daLiJeProst(x) == True:
    print('\nProst je!')
else:
    print('\nNije prost!')

    
    





    





