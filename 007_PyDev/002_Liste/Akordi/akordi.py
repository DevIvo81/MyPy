'''
Program:    Generator akorda
Autor:      Ime prezime
Verzija:    0.1
'''

'''
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23
C   C#  D   D#  E   F   F#  G   G#  A   A#  H   C   C#  D   D#  E   F   F#  G   G#  A   A#  H

E ili E dur     E G# H
G ili G dur     G H D


H ili H dur     H D# F#
'''

tonovi = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

print('\tGenerator akorda\n')
print('Lista svih tonova od kojih mozete generirati akord:')

for ton in tonovi:
    print(ton, end=' ')
print('\n')

tonovi.extend(tonovi)

pocetni_ton_akorda = input('Upisite pocetni ton zeljenog akorda:\t')
pocetni_ton_akorda = pocetni_ton_akorda.upper()

indeks_pocetnog_tona = tonovi.index(pocetni_ton_akorda)

print(f'Durski akord {pocetni_ton_akorda} tona cine:')
print(f'Naziv akorada: {pocetni_ton_akorda} ili {pocetni_ton_akorda} dur')
print(f'\t{pocetni_ton_akorda} kao prvi ton,')
print(f'\t{tonovi[indeks_pocetnog_tona + 4]} kao drugi ton,')
print(f'\t{tonovi[indeks_pocetnog_tona + 7]} kao treci ton.')

print(f'Moliski akord {pocetni_ton_akorda} tona cine:')
print(f'Naziv akorada: {pocetni_ton_akorda.lower()} ili {pocetni_ton_akorda.lower()} mol')
print(f'\t{pocetni_ton_akorda} kao prvi ton,')
print(f'\t{tonovi[indeks_pocetnog_tona + 3]} kao drugi ton,')
print(f'\t{tonovi[indeks_pocetnog_tona + 7]} kao treci ton.')


# tonovi_1 = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
# print(*tonovi_1)