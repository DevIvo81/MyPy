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

def uvodIVracanjeTonova():

    tonovi = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

    print('\n\t\tAKORDOTVORAC\n')
    print('Lista svih tonova od kojih mozete generirati akord:\n')
    print(*tonovi, sep = ' ')
    print()
    tonovi.extend(tonovi)
    return tonovi


def akordomat(tonoviIzUvoda):
        
    pocetni_ton_akorda = input('\nUpisite pocetni ton zeljenog akorda --> ')
    
    if pocetni_ton_akorda.isupper():
        
        print(f'\nOdabran je {pocetni_ton_akorda} - dur')
        indeks_pocetnog_tona = tonoviIzUvoda.index(pocetni_ton_akorda.upper())
        print(f'{pocetni_ton_akorda} - dur glasi --> {pocetni_ton_akorda} -- {tonoviIzUvoda[indeks_pocetnog_tona + 4]} -- {tonoviIzUvoda[indeks_pocetnog_tona + 7]}')
        
    else:
        
        print(f'\nOdabran je {pocetni_ton_akorda} - mol')
        indeks_pocetnog_tona = tonoviIzUvoda.index(pocetni_ton_akorda.upper())
        print(f'\n{pocetni_ton_akorda} - mol glasi --> {pocetni_ton_akorda} -- {tonoviIzUvoda[indeks_pocetnog_tona + 3]} -- {tonoviIzUvoda[indeks_pocetnog_tona + 7]}')

while True:
    
    tonoviIzUvoda = uvodIVracanjeTonova()
    
    akordomat(tonoviIzUvoda)

    if input('\nJoš jedan akord? ["n" za izlaz] --> ').lower() == 'n':
        print('\nDo sljedećeg puta, pozdrav!\n')
        break


