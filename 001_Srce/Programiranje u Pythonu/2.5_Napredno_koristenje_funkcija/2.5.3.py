'''3.  Napišite bezimenu funkciju koja prima 3 vrijednosti 
(pretpostavimo da su sve tri vrijednosti pozitivne i strogo veće od 
0). Ta bezimena funkcija izračunava i vraća rezultat matematičke 
formule: (a*b + c) / c. U glavnom programu ispišite rezultat 
matematičke formule za sljedeće vrijednosti: a = 5, b = 10; c = 2.'''
import os
os.system('cls')

a = int(input('\nUpiši broj "a": '))
b = int(input('\nUpiši broj "b": '))
c = int(input('\nUpiši broj "c": '))

if c == 0:
    print('Err!')
else:
    f = lambda a, b, c: (a*b + c) / c
    print(f'\nRezultat bezimene funkcije za a = {a}, b = {b} i c= {c} je {f(a, b, c)}')

'''4.  Nadogradite prethodni zadatak tako da prethodno 
implementirana bezimena funkcija može primiti 3 vrijednosti u 
rasponu od <-∞, ∞>. Ako izračun nije moguće provesti, ispišite 
poruku: "Err!", u suprotnom ispišite rezultat matematičke formule. 
Napomena: obradite slučaj dijeljenja s 0. '''