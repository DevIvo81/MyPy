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

baza_vozila = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.99],
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.99],
    3: ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78000.99],
    4: ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97000.99],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.99],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.99],
    7: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.99],
    8: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.99],
    9: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.99],
    10: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.99],
    11: ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78000.99],
    12: ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97000.99],
    13: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.99],
    14: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.99],
    15: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.99],
    16: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.99]
}

print()
print('_' * 90)
header_top_line = f'ID\tTip\t\tProizvodac\tRegistarska\tGodina prve\tCijena'
header_bottom_line = f'  \t   \t\t          \toznaka\t\tregistracije\t(EUR)'
print(header_top_line, '\n', header_bottom_line)
print('_' * 90, '\n')


for id, vozilo in baza_vozila.items():
    print(f'{id}', end='\t')

    for podatak_o_vozilu in vozilo:
        if type(podatak_o_vozilu) == str:
            if len(podatak_o_vozilu) > 7:
                print(f'{podatak_o_vozilu}', end='\t')
            else:
                print(f'{podatak_o_vozilu}', end='\t\t')
        else:
            print(f'{podatak_o_vozilu}', end='\t\t')

    print()

print('_' * 90, '\n')