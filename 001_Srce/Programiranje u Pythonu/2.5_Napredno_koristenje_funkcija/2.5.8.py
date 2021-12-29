'''8.  * Napišite program koji će od korisnika tražiti dvije 
vrijednosti. Prva vrijednost neka bude neki proizvoljan cijeli 
broj, a druga vrijednost neka bude znamenka od 0 do 9. 
Kreirajte rekurzivnu funkciju koja će odrediti broj pojavljivanja 
zadane znamenke u zadanom broju. 
Prototip funkcije:  prebroji(broj, znamenka)'''
import os
os.system('cls')

def prebroji(broj, znamenka):
    if broj == 0:
        return 0
    elif str(znamenka) in str(broj):
        return str(broj).count(str(znamenka))
    else:
        return prebroji(broj // 10, znamenka)

# GLAVNI PROGRAM -- UNOS
while True:
    broj = input('\nUnesi cijeli broj: ')
    if broj.isalpha() == True:
        print(f'\nBroj! U {broj} ima slova!')
    
    znamenka = input('\nUnesi znamenku koju tražimo [0->9]: ')
    if znamenka.isalpha() == True:
        print(f'\nBroj! U {znamenka} ima slova!')
    elif 0 > int(znamenka) or int(znamenka) > 9:
        print(f'\nZnamenka nije iz raspona [0->9]')
    
    else:
        broj = int(broj)
        znamenka = int(znamenka)
        break

f = prebroji(broj, znamenka)

print(f)

    