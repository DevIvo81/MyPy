'''4.  Napišite funkciju koja prima 2 parametra. Rezultat 
izračuna funkcije ovog puta se ne ispisuje izravno u 
funkciji nego u glavnom dijelu programa. 
Funkcija mora izračunati rezultat formule:
(a*a) + (b*b)'''

import os
os.system('cls')

def rezultat(a, b):
    return (a*a + b*b)

rez = rezultat(5,10)
print("\nRezultat formule (a*a) + (b*b) za a=5 i b=10, iznosi ", rez)
