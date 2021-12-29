baza_vozila = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.99],
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.99],
    3: ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78000.99],
    4: ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97000.99],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.99],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.99],
    7: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.99],
    8: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.99]
}

print('PRIJE')
for id, vozilo in baza_vozila.items():
    print(f'{id}', end=' ')
    for podatak_o_vozilu in vozilo:
        print(f'{podatak_o_vozilu}', end=' ')
    print()


# CLEAR()
# help(dict)
# baza_vozila.clear()

# print('\n\nNAKON CLEAR()')
# for id, vozilo in baza_vozila.items():
#     print(f'{id}', end=' ')
#     for podatak_o_vozilu in vozilo:
#         print(f'{podatak_o_vozilu}', end=' ')
#     print()
# print(baza_vozila)

# POP()
# print('\n\nNAKON POP()')


# vrijednost_iz_pop = baza_vozila.pop(15, 'Ne postoji element s unesenim indeksom!')
# print('POP(15)', vrijednost_iz_pop)

# for id, vozilo in baza_vozila.items():
#     print(f'{id}', end=' ')
#     for podatak_o_vozilu in vozilo:
#         print(f'{podatak_o_vozilu}', end=' ')
#     print()

# help(dict.pop)

#POPITEM()
#help(dict.popitem)

# vraceni_element = baza_vozila.popitem()
#print('\n\nNAKON POPITEM()')
# print('POPITEM()', vraceni_element)

# for i in range(len(baza_vozila)):
#     vraceni_element = baza_vozila.popitem()
#     print('POPITEM()', vraceni_element)

# print('\n\n')
# print(baza_vozila)
# for id, vozilo in baza_vozila.items():
#     print(f'{id}', end=' ')
#     for podatak_o_vozilu in vozilo:
#         print(f'{podatak_o_vozilu}', end=' ')
#     print()

