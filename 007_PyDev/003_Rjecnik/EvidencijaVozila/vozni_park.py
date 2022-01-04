'''
Kreirajte bazu s vozilima firme. 
ID svakog retka je cijeli broj, 
a podaci koji se čuvaju o svakom vozilu su: 
tip, proizvođač, registarska oznaka, 
godina prve registracije te cijena u eurima.

Ispišite cijelu tablicu tako da ID odvojite od ostatka retka
jednim TABom, a druge informacije formatirajte tako da
prvi red tablice predstavlja naslovni red, 
a ostali redovi tablice predstavljaju podatke iz baze.
'''
import os
os.system('cls')

baza_vozila = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.99],
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.99],
    3: ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78000.99],
    4: ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97000.99],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.99],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.99],
    7: ['Dostavno', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.99],
    8: ['Dostavno', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.99]
}

print(f'ID\tTip\t\tProizvođač\tRegistarska\tGodina prve\tCijena u EUR')
print(f'\t\t\t\t\toznaka\t\tregistracije\n')

for id, vozilo in baza_vozila.items():
    print(f'{id}', end='\t')
    for podatak_o_vozilu in vozilo:
        if len(str(podatak_o_vozilu)) <= 7:
            print(f'{podatak_o_vozilu}', end='\t\t')
        else:
            print(f'{podatak_o_vozilu}', end='\t')
    print()


broj_novih_vozila = int(input('\nUpisite koliko vozila zelite dodati? --> '))

for i in range(broj_novih_vozila):
    id = len(baza_vozila) + 1
    vozilo = []

    tip = input('Upisite tip vozila: ')
    vozilo.append(tip)
    
    proizvodac = input('Upisite naziv proizvodaca vozila: ')
    vozilo.append(proizvodac)
    
    reg_oznaka = input('Upisite registarsku oznaku vozila: ')
    vozilo.append(reg_oznaka)
    
    godina_prve_reg = int(input('Upisite godnu prve registaracije vozila: '))
    vozilo.append(godina_prve_reg)

    cijena = float(input('Upisite cijenu vozila: '))
    vozilo.append(cijena)

    baza_vozila[id] = vozilo


for id, vozilo in baza_vozila.items():
    print(f'{id}', end=' ')
    for podatak_o_vozilu in vozilo:
        print(f'{podatak_o_vozilu}', end=' ')
    print()
