'''1. Napravite listu imena dani s popisom radnih dana u tjednu (od 
ponedjeljka do petka). Budući da listi nedostaje vikend (subota i 
nedjelja), dodajte ga te ispišite listu.

2. Napravite dvije liste, jednu imena radniDani(od ponedjeljka do 
petka) te drugu listu imena dani(od ponedjeljka do nedjelje). 
Na temelju te dvije liste popunite listu imena vikend.

3.  Napravite dvije liste, jednu imena dani(od ponedjeljka do petka) te 
drugu listu imena vikend(subota i nedjelja). Koristeći metodu 
extendspojite liste danii vikend.'''

import os
os.system('cls')

dani = ['Ponedjeljak', 'Utorak', 'Srijeda', 'Četvrtak', 'Petak']
vikend = []

radni_dani = dani.copy()

dani.append('Subota')
dani.append('Nedjelja')

print('\nDani u tjednu:')
print('\n', dani, '\n')

print('\nRadni dani:')
print('\n', radni_dani, '\n')

for e in dani:
    if e not in radni_dani:
        vikend.append(e)
   
print('\nVikend:')
print('\n', vikend, '\n')

radni_dani.extend(vikend)

print('\nRadni dani + Vikend:')
print('\n', radni_dani, '\n')
