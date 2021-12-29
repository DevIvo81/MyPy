'''8. * Napišite program koji s tipkovnice učitava cijeli broj niz intervala [3, 
20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu 
poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon 
učitane vrijednosti n, učitajte nparova cijelih brojeva. Nakon što je n 
parova brojeva učitano, ispišite parove brojeva koji imaju najveću 
sumu.'''
import os
os.system('cls')

while True:
    n = int(input('\nUnesite broj [3,20]: '))
    if 3<= n <= 20:
        break
    else:
        print('\nGreška, probaj opet!')

i = 0    
lista=[]
max_suma = 0

while i < n:
    print(i+1,'.par', sep='')

    x = int(input('\nUnesite broj x: '))
    y = int(input('\nUnesite broj y: '))

    lista.append([x, y])

    if  max_suma < x+y:
        max_suma = x+y
        
    i += 1

for e in lista:
    if e[0] + e[1] == max_suma:
        print('\nPar sa najvećom sumom je: ', e)
        print()
        print(e[0], '+', e[1])
print()
print(lista)

