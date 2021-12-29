'''4.  * Napišite program koji učitava cijele brojeve sve dok je unesena 
vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju 
sumu znamenki te ispišite taj broj i sumu.'''
import os
os.system('cls')

print('\nAko je "broj <= 0" program završava!')

def sumaZnamenaka(a):
    suma = 0
    while a > 0:
        suma += a%10
        a //= 10
    return suma

broj_min = 0
suma_min = -1

while True:
    a = int(input('\nUpišite broj: '))
    if a <= 0:
        break
    else:
        s = sumaZnamenaka(a)
    
    
    if suma_min == -1 or suma_min > s:
        suma_min = s
        broj_min = a


print('\nBroj: ', broj_min)
print('\nSuma znamenaka: ', suma_min)
