'''
Kreirajte aplikaciju za izradu računa
Uz svaki račun čuvajte sljedeće podatke:
    Broj računa
    
'''

racunBroj = 'R-1-2022-01'
racunDatumIzdavanja = '14.01.2022.'
racunStavke = {
    'Laptop' : 4599.99,
    'Torba za laptop' : 659.99,
    'Monitor' : 4599.99,
    'Python za početnike' : 4599.99
}

racunUkupanIznos = 0

for stavkaCijena in racunStavke.values():
    racunUkupanIznos += stavkaCijena

racunIznosPdv = racunUkupanIznos * 0.25
racunUkupnoPdv = racunUkupanIznos + racunIznosPdv

# ISPIS

print(f'Racun br.\t{racunBroj}')
print(f'Datum izdavanja racuna\t{racunDatumIzdavanja}')
print('STAVKE')
print(racunStavke)


