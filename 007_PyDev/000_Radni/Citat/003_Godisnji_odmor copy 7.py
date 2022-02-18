import os
from Proba import rjecnikStavki, jeLiInteger
os.system('cls')

opcije = {}

if input('\nNova opcija? (D za dodavanje) --> ').lower() != 'd':
    print('\nDoviđenja!\n')
else:
    
    brojOpcija = jeLiInteger('\nKoliko novih opcija? --> ')
    
    for i in range(brojOpcija):
        
        while True:
            
            odrediste = input('\nDestinacija? --> ').upper()
            
            if odrediste in opcije.keys():
                print('\nTa opcija već postoji!')
                continue
            else:
                
                opcije[odrediste] = rjecnikStavki()
                break
    print('\nUNOS DESTINACIJA ZAVRŠEN\n')




print('\n##############')
print('KRAJ PROGRAMA')   
print('##############\n')