'''9.  ** Izradite listu koja se sastoji od trojki brojeva od 1 do 40 koje 
zadovoljavaju izraz: 𝑥2 + 𝑦2 = 𝑧.'''
import os
os.system('cls')

lista = []

for x in range(1, 41):
    for y in range(1, 41):
        for z in range(1, 41):
            if (x*x + y*y) == z:
                trojka = [x, y, z]
                lista.append(trojka)

for i in range(len(lista)):
    print(lista[i])