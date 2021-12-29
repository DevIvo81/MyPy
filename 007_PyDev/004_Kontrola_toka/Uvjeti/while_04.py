### POGODI BROJ ###
# Sjećate se Računalnog razmišljanja i pogađanja broja između 1 i 100.
# Sada imate dovoljno znanja da napišete
# program koji će Vam omogućiti pogađanje broja

import random
import os
os.system('cls')

zamisljeni_broj = random.randint(1, 100)
broj_pokusaja = 0
# print(zamisljeni_broj, '\n')

# lista_brojeva = [ broj for broj in range(1, 21) ]
# promijesana_lista_brojeva = random.shuffle(lista_brojeva)

# for br in lista_brojeva:
#     print(br, end=' ')

while True:
    print()

    uneseni_broj = int(input('Pogodi broj koji sam zamislio od 1 do 100. '))
    broj_pokusaja += 1

    if uneseni_broj == zamisljeni_broj:
        print()
        print('!!! CESTITAM!!!')
        print(
            f'Zamisljeni broj {zamisljeni_broj} ste pogodili iz {broj_pokusaja}')
        print()
        break
    elif uneseni_broj > zamisljeni_broj:
        print()
        print(f'Broj {uneseni_broj} je VECI od zamisljenog broja')
        print()
    elif uneseni_broj < zamisljeni_broj:
        print()
        print(f'Broj {uneseni_broj} je MANJI od zamisljenog broja')
        print()
