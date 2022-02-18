# import datetime

from datetime import datetime as dt
from random import randint as rnd
import os
os.system('cls')


danasnjiDatum = dt.now()
print(f'Ispis PRIJE funkcije {danasnjiDatum}')
godina = rnd(2001, 2022)
print(f'Ispis PRIJE funkcije {godina}')

def pozdrav(
    parametar_ime = 'Ime nepoznate osobe', 
    parametar_prezime = 'Prezime nepoznate osobe', 
    parametar_godinaRodenja = godina):
    
    if danasnjiDatum.minute < 30:
        print(f'{parametar_ime} {parametar_prezime}, još malo do 45')
    elif danasnjiDatum.minute > 30:
        print(f'{parametar_ime} {parametar_prezime}, još malo do 45')
    else:
        print(f'{parametar_ime} {parametar_prezime}, još malo do 45')
    
    print(f'Godina rođenja {parametar_godinaRodenja}')
    godina = 2022
    print(f'Ispis IZ funkcije {godina}')
    print('\n\n')

def pozdrav_return(
    parametar_ime = 'Ime nepoznate osobe', 
    parametar_prezime = 'Prezime nepoznate osobe', 
    parametar_godinaRodenja = 1998):
    
    if danasnjiDatum.minute < 30:
    print(f'Dobar dan {parametar_ime} {parametar_prezime}')
    print(f'Godina rođenja {parametar_godinaRodenja},', end='\n\n', sep=':')
    
    godina = 2022
    print(f'Ispis IZ funkcije {godina}')


imeOsobe = 'Pero'
prezimeOsobe = 'Perić'
godinaRodenja = 1999
pozdrav()

# pozdrav(imeOsobe, prezimeOsobe, godinaRodenja)

# # Redoslijed je bitan!
# pozdrav(godinaRodenja, prezimeOsobe, imeOsobe)

# # Ali ako se definiraju parametri onda nije!

pozdrav(
    parametar_godinaRodenja=godinaRodenja,
    parametar_ime=imeOsobe,
    parametar_prezime=prezimeOsobe,
)

rezultatIzFunkcije = pozdrav_return(
                                
)
    