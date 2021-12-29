'''Napišite funkciju koja prima 4 parametara. Funkcija mora ispisati 
rezultat matematičke formule:
( (a*a) + (b*c) – d ) / 2
U glavnom dijelu programa pozovite napisanu funkciju.'''

import os
os.system('cls')

def rezultat(a, b, c, d):
    print((a*a + b*c-d)/2)

print()
rezultat(5, 10, 15, 25)