'''6. Napišite funkciju koja prima listu. Funkcija vraća boolean vrijednost 
istina ako su svi elementi liste parni brojevi, a boolean vrijednost laž 
ako postoji barem jedan broj koji nije paran.'''
import os
os.system('cls')

def lista():
    istina = True
    parni = 'Svi uneseni brojevi su parni!'
    brojevi = []
    for i in range(6):
        broj = input('\nUpiši broj: ')
        brojevi.append(broj)
    
    for broj in brojevi:
        if int(broj) % 2 != 0:
            istina = False
            laz = 'Barem jedan broj je neparan!'
    
    if istina == False:
        return print(istina, laz, brojevi)
    else:
        return print(istina, parni, brojevi)

lista()









    
