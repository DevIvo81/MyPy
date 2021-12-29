'''Kreirajte listu imena pomoću recimo ovakvog online name generatora 
(https://www.behindthename.com/random/). 

- Ispišite jedno po jedno ime, u istoj liniji odvojeno ; znakom. 

- Pomoću FOR petlje dodajte još 3 imena u listu. 

- Kreirajte novu listu i u nju upišite sva imena iz prethodne liste 
 ali ne kao slova, nego kao brojeve iz ASCII table (https://www.asciitable.com/).

Kreirajte program koji će ispisati ASCII tabelu kao na prethodnom linku jedino 
ne trebate dodavati „html“ stupac.

Kreirajte program koji će za brojeve od 0 do broja kojeg definira korisnik ispisati 
dekadski, oktalni, heksadekadski, binarni i ASCII znak. Svaki od ovih oblika pohranite u zasebnu listu.'''

import os
os.system('cls')

imena_1 = ['Javor', 'Denis', 'Maja', 'Anamarija', 'Damir']
print()

for ime in imena_1:
    print(ime, end=' ; ')

print()

imena_2 = ['Josip', 'Ivo', 'Ana']

for ime in imena_2: # dodavanje 3 nova imena u listu
    imena_1.append(ime)
print()
print(imena_1)
print()

asci_lista = []

# iteracija po imenima
for ime in imena_1:   
# iteracija po slovima u pojedinačnom 
# imenu i kreiranje liste, gdje su elementi 
# zasebne liste sa ASCII kodovima slova imena
    asci_lista.append([ord(slovo) for slovo in ime])    

print()
print(*asci_lista, sep = '\n')
print()
# provjera da li su liste iste duljine           
print(len(imena_1) == len(asci_lista))
print()

# ispis liste ASCII kodova

print('DEC\t HEX\t OCT\t CHR')
print('----------------------------')
print()
for i in range(128):
    if i == 0:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'NUL')
    elif i == 7:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'BEL')
    elif i == 8:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'BSPC')
    elif i == 9:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'TAB')
    elif i == 10:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'LF')
    elif i == 11:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'VT')
    elif i == 12:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'FF')
    elif i == 13:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'CR')
    elif i == 14:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'SO')
    elif i == 15:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'SI')
    elif i == 27:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'ESC')
    elif i == 28:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'FS')
    elif i == 32:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'SPACE')
    elif i == 127:
        print(i, '\t',hex(i), '\t', oct(i), '\t', 'DEL')
    else:
        print(i, '\t',hex(i), '\t', oct(i), '\t',chr(i))

# Kreirajte program koji će za brojeve od 0 do 
# broja kojeg definira korisnik ispisati dekadski, 
# oktalni, heksadekadski, binarni i ASCII znak. 
# Svaki od ovih oblika pohranite u zasebnu listu.

n = int(input('\nUpiši cjelobrojnu gornju granicu raspona: '))

dek = [i for i in range(n+1)]
print(f'\nDekadska lista: {dek}')
heks = [hex(i) for i in range(n+1)]
print(f'\nHeksadekadska lista: {heks}')
okt = [oct(i) for i in range(n+1)]
print(f'\nOktalna lista: {okt}')
aski = [chr(i) for i in range(n+1)] 
print(f'\nASCII lista: {aski}')

