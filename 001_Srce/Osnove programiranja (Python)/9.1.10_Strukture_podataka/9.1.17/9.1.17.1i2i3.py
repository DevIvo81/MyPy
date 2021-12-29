'''1.  Napišite listu gradovi s barem pet gradova. Na toj listi isprobajte 
metode reverse() i sort().

2.  Napišite listu gradovi s barem pet gradova. Programski odredite 
ime grada koji se nalazi na kraju liste. Tako određen grad nadodajte 
na prvu poziciju u listi gradovite ispišite listu. Iz liste gradovi 
izbacite sva pojavljivanja zadnjeg grada te ponovo ispišite listu.

3.  Napišite listu gradovis barem pet gradova. Ispišite sve elemente 
liste gradovi tako da se svaki nalazi u svom retku.'''
import os
os.system('cls')

gradovi = ['Zagreb', 'Kutina', 'Vodice', 'Osijek', 'Split']

print('\nLista gradova:')
print('\n', gradovi, '\n')

gradovi.sort()
print('\nSortirano po imenu:')
print('\n', gradovi, '\n')

gradovi.reverse()
print('\nSortirano unatrag:')
print('\n', gradovi, '\n')

#gradovi = ['Zagreb', 'Kutina', 'Vodice', 'Osijek', 'Split']


