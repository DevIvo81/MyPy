'''1.  Napišite program koji se sastoji od liste. Elementi liste neka budu 
proizvoljnih vrijednosti. Ispišite samo one elemente koji se nalaze na 
parnom indeksu.'''
import os
os.system('cls')

lista = [i for i in range(20)]
print(lista)
print()
print(lista[::2])
        