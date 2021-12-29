'''1. Napravite rječnik osoba s ključevima ime, prezime, godine. 
Vrijednosti pridružene ključevima odredite sami. Ispišite samo 
vrijednosti u rječniku koristeći "for" petlju.

2.  U rječnik kreiran u prethodnom zadatku dodajte novi par 
{ključ:vrijednost}. Ključ može biti adresa, OIB ili nešto slično.

3.  Iz rječnika korištenog u prethodnom zadatku izbrišite element 
"godine" te ispišite rječnik.'''
import os
os.system('cls')

osoba = { 'Ime' : 'Ivo', 'Prezime' : 'Zelić', 'godine' : '40'} 
for e in osoba.values():
    print(e)

print()

osoba.update({'OIB' : '06631772127'})
for e in osoba.values():
    print(e)

print()

del osoba['godine']
for e in osoba.values():
    print(e)




