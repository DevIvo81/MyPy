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

def ispis():
    from os import system as s
    s('cls')
    
    naslovSrednjiRed = f'ID\tTip\t\tProizvođač\tRegistarska\tGodina prve\tCijena u EUR'
    print((((len(naslovSrednjiRed)//2)+5) * ' ') + 'BAZA VOZILA\n')
    print(naslovSrednjiRed)
    print(f'\t\t\t\t\toznaka\t\tregistracije\n')

    for id, vozilo in baza_vozila.items():
        print(f'{id}', end='\t')
        for podatak_o_vozilu in vozilo:
            if len(str(podatak_o_vozilu)) <= 7:
                print(f'{podatak_o_vozilu}', end='\t\t')
            else:
                print(f'{podatak_o_vozilu}', end='\t')
        print()




def upisNovogVozila(broj_novih_vozila):
    
    for i in range(broj_novih_vozila):
        id = len(baza_vozila) + 1
        vozilo = []

        tip = input('Tip vozila: ')
        vozilo.append(tip)
        
        proizvodac = input('Proizvođač vozila: ')
        vozilo.append(proizvodac)
        
        reg_oznaka = input('Registarska oznaka vozila: ')
        vozilo.append(reg_oznaka)
        
        godina_prve_reg = int(input('Godina prve registracije: '))
        vozilo.append(godina_prve_reg)

        cijena = float(input('Upišite cijenu vozila: '))
        vozilo.append(cijena)

        baza_vozila[id] = vozilo



# Glavni program

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

ispis()

while True:
        
    broj_novih_vozila = input('\nUpišite koliko vozila želite dodati? --> ')
    if broj_novih_vozila.isdigit() == False or broj_novih_vozila == '':
        print('\nPogrešan unos, pokušajte ponovno!')
        
    else:
        broj_novih_vozila = int(broj_novih_vozila)
        upisNovogVozila(broj_novih_vozila)
        ispis()
    
    if input('\nŽelite li dodati još vozila? ["0" za izlaz] --> ') == '0':
        print('\nDo sljedećeg puta, pozdrav!\n')
        break