'''10. ** S tipkovnice učitajte pozitivne realne brojeve a, b i cijeli broj n. 
Brojevi "a i "b" predstavljaju početne članove nizova A i B (𝑎1 odnosno 
𝑏1), dok broj n predstavlja broj koraka izračunavanja. Član niza 𝑎𝑖 izračunava 
se kao aritmetička sredina prethodnog člana niza A i 2 prethodnog člana niza B, 
tj. 𝑎𝑖  = 𝑎𝑖−1+𝑏𝑖−1 / 2  . Član niza 𝑏𝑖 izračunava se kao geometrijska sredina 
prethodnog člana niza A i prethodnog člana niza B, tj. √𝑎𝑖−1 + 𝑏𝑖−1. Članove 
nizova A i B ispišite u skladu s oblikom ispisa prikazanog u nastavku. 
Prilikom ispisa, vrijednosti elemenata niza 𝑎𝑖 i 𝑏𝑖 zaokružite na dvije decimale.
Unesite vrijednost a1: {vrijednost}
Unesite vrijednost b1: {vrijednost}
Unesite vrijednost n: {vrijednost} 
A(1) = {vrijednost}, B(1) = {vrijednost}
Napomena: prethodnu liniju potrebnu je ponoviti n puta, a kao 
vrijednosti ispišite vrijednosti dobivene prema zadanim 
formulama.'''
import os, math
os.system('cls')

a = float(input('\nUpiši realni broj "A": '))
b = float(input('\nUpiši realni broj "B": '))
n = int(input('\nUpiši broj ponavljanja operacije "n": '))

print('A(1) = ', round(a, 2), sep = '', end = ', ')
print('B(1) = ', round(b, 2))

i = 2

while i < n:

    a_priv = a
    b_priv = b
    a = (a_priv + b_priv) / 2
    b = math.sqrt(a_priv + b_priv)

    print('A(', i, ') =', round(a, 2), sep='', end=', ')
    print('B(', i, ') =', round(b, 2), sep='')

    i += 1




