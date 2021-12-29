'''7.  Implementirajte generatorsku funkciju imena jedanDvaTri() 
koja vraća generator koji pak vraća vrijednosti: "Jedan", "Dva", 
"Tri", "Jedan", "Dva", "Tri", "Jedan", "Dva", "Tri" i tako u 
beskonačnost. U glavnom programu ispišite proizvoljan broj puta 
sekvencu: "Jedan", "Dva", "Tri".'''
import os
os.system('cls')

def jedanDvaTri():
    while True:
        yield print('"Jedan", "Dva", "Tri", ')

# x = input('\nUpiši broj ponavljanja: ')
# x = int(x)

g = jedanDvaTri()
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)