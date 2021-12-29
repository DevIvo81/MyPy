'''6.  Implementirajte dvije funkcije. Prva funkcija neka se zove 
paran()i ona neka ispisuje na ekran: "Paran!", druga funkcija 
neka se zove neparan()i ona neka ispisuje na ekran: 
"Neparan!". S tipkovnice učitajte broj proizvoljne vrijednosti te 
pomoću ternarnog operatora detektirajte je li učitana vrijednost 
parna ili neparna te ovisno o parnosti pozovite jednu od dviju 
funkcija koje ste prethodno kreirali.'''
import os
os.system('cls')

broj = int(input('\nUpiši broj: '))

def paran():
    return print('\nParan!')

def neparan():
    return print('\nNeparan!')

paran() if broj % 2 == 0 else neparan()

