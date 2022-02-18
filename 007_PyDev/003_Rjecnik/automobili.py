import os
os.system('cls')

# print('ID\tTip\t\tProizvođač\tRegistarska oznaka\tPrva Reg.\tCijena (EUR)')
# print('______________________________________'*2)

# auti = {1 : '\tKamion\t\tIveco\t\tOS 001 ZZ\t2015\t\t45.000', 
#         2:  '\tKamion\t\tIveco\t\tOS 002 ZZ\t2015\t\t47.000', 
#         3 : '\tTegljač\t\tMAN\t\tRI 001 ZZ\t2015\t\t78.000', 
#         4 : '\tTegljač\t\tMAN\t\tRI 001 ZZ\t2015\t\t97.000', 
#         5 : '\tKombi\t\tMercedes\tST 001 ZZ\t2015\t\t12.000', 
#         6 : '\tKombi\t\tVolkswagen\tST 001 ZZ\t2015\t\t35.000', 
#         7 : '\tDostavno\tVolkswagen\tZG 001 ZZ\t2015\t\t9.000', 
#         8 : '\tDostavno\tVolkswagen\tZG 001 ZZ\t2015\t\t9.000'}

# for auto in auti.values():
#     print(auto)
# print()
# print()

baza_vozila = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000], 
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000],
    3: ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000],
    4: ['Kamion', 'MAN', 'RI 002 ZZ', 2020, 97000],
    5: ['Kamion', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000],
    6: ['Kamion', 'Volkswagen', 'ST 002 ZZ', 2021, 35000],
    7: ['Kamion', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000],
    8: ['Kamion', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300]
}

print()
print('ID\tTip\t\tProizvođač\tRegistarska\tGodina prve\tCijena u EUR')
print('  \t   \t\t          \toznaka     \tregistracije')
print()


for id, vozilo in baza_vozila.items():
    
    print(f'{id}', end='\t')
    
    for podatak_o_vozilu in vozilo:
        
            print(f'{podatak_o_vozilu}', end='\t')
        else:
            print(f'{podatak_o_vozilu}', end=' ')    
        

# broj_novih_vozila = int(input('Upišite koliko vozila želite  unijeti: '))
# for i in range(broj_novih_vozila):
#     id = len(baza_vozila) + 1
#     vozilo = []


#     tip = input('Upišite tip vozila: ')
#     vozilo.append(tip)

#     proizvodac = input('Upišite proizvođača vozila: ')
#     vozilo.append(proizvodac)
        
#     reg_Oznaka = input('Upišite registarsku oznaku vozila: ')
#     vozilo.append(reg_Oznaka)

#     godina_Prve_Reg = input('Upišite godinu prve registracije vozila: ')
#     vozilo.append(godina_Prve_Reg)

#     cijena = input('Upišite cijenu vozila: ')
#     vozilo.append(cijena)

#     baza_vozila[id] = vozilo

# for id, vozilo in baza_vozila.items():
#     print(f'{id}', end='\t')
#     for podatak_o_vozilu in vozilo:
#         print(f'{podatak_o_vozilu}', end='\t')
#     print()
        

# print('PRIJE POP()')
# for id, vozilo in baza_vozila.items():
#     print(f'{id}', end='\t')
#     for podatak_o_vozilu in vozilo:
#         print(f'{podatak_o_vozilu}', end='\t')
#     print()

# CLEAR()
# help(dict)
# baza_vozila.clear()


# POP()
# help(dict.pop)

# print('NAKON POP()')

# vrijednost_iz_pop = baza_vozila.pop(15, 'Nepostoji element s unesenim indeksom')
# print('POP(15)', vrijednost_iz_pop)

# for id, vozilo in baza_vozila.items():
#     print(f'{id}', end='\t')
#     for podatak_o_vozilu in vozilo:
#         print(f'{podatak_o_vozilu}', end='\t')
#     print()
