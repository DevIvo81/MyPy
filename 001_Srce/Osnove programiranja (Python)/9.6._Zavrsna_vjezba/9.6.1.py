'''1.  * S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo 
koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo 
veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva 
osim broja zbog kojeg je prekinuto učitavanje.'''
import os
os.system('cls')

print('\nUnosimo brojeve. Upis manjeg broja od prethodnog završava program')
print('i ispisuje sumu brojeva.')

suma = 0
dosad_upisano = []
kontrola = True

while kontrola == True:
    
    broj = input('\nUnesi broj: ')
    suma += int(broj)
    dosad_upisano.append(broj)
    
    for i in range(1, len(dosad_upisano)):
        
        if int(dosad_upisano[i]) < int(dosad_upisano[i-1]):
            suma -= int(broj)
            print ('\nPREKID!. Suma unesenih brojeva iznosi suma = ', suma)
            print('\n Uneseni brojevi su ', dosad_upisano)
            
            kontrola = False
input()
            



     


