'''* Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni 
niz znakova i brojčanu varijablu n. Provjerite je li vrijednost varijable 
"n" manja od broja znakova u nizu. Ako je vrijednost varijable "n" veća 
ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to 
slovo. Na primjer, ulazni niz je "ABCDEFGH", nje 2, tada je izlaz 
"ACEG".'''

import os
os.system('cls')

a = "AnteITenaSuBratISestra"

print()
print(a)
print()

while True:
    n = int(input('\nUnesi željeni korak ispisa "n": '))
    
    if n >= len(a) :
        print("\nUneseni korak je veći ili jednak duljini niza! Pokušaj ponovno!")
    else:
        print("Svako, ", n,". slovo niza je: ", end=' ')
        for i in range(0, len(a), n):
            print(a[i], end=' ')
        break



