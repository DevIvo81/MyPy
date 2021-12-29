'''4.  Kreirajte listu te ju popunite s 5 proizvoljnih vrijednosti (brojeva). 
Nakon toga učitajte proizvoljnu vrijednost (broj) s tipkovnice. 
Unutar petlje for provjerite  nalazi li se vrijednost koju ste učitali 
s tipkovnice unutar liste. Ako tražena vrijednost (broj) postoji u 
listi, ispišite na ekran "Postoji!", u suprotnom ispišite na ekran 
"Ne postoji!".'''
import os
os.system('cls')

lista = [i for i in range(10,51,10)]
print(lista)

element = int(input('\nUpiši broj: '))
broj = element

for element in lista:
    if element == broj:
        print('\nPostoji!')
        break
else:
    print('\nNe postoji!')
