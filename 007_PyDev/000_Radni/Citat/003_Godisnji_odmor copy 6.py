import os, locale
from Funk import *




def jednaOpcija(): 
    
    def popisTroskova():
        
        popisStavki = obradaListeTroškova()

        inputString = 'Upiši cijenu za'

        troskovi = listaTroskova(popisStavki, inputString)

        troskoviPlusTOTAL = dodajTOTAL(troskovi)
        
        return troskoviPlusTOTAL
    
    
    while True:        
        
        upis = input(f'\nUpiši odredište --> ').upper()
        # Ako smo išta upisali
        
        if upis:
            jednaOpcija = [upis, popisTroskova()]
            break
        
    
    return jednaOpcija

#listaJedneOpcije = jednaOpcija()
# print(*listaJedneOpcije[0])   
# print(*listaJedneOpcije[1], sep='\n')    

   
def GOLista():  

    popisOpcija = []
    
       
    upit = input('\nDodavanje opcije? (ENTER za izlaz) --> ').lower()
    
    if not upit:
        print('\nPOZDRAV!\n')
        return popisOpcija

    else:
            
        brojOpcija = jeLiInteger('\nKoliko novih opcija? --> ')

        for i in range(brojOpcija):
                
            popisOpcija.append(jednaOpcija())
            
        print('\n---------------------------')
        print('UNOS OPCIJA ZAVRŠEN')
        print('---------------------------')

    return popisOpcija
  

# popisOpcija = GOLista()

def ispisStavki(popisOpcija):
    
    for i in range(len(popisOpcija)):
        print(popisOpcija[i][0])
        print()
        print(*popisOpcija[i][1], sep='\n')
        print()
    return popisOpcija



def spremiUFile():
    zaUFajl = ispisStavki()
    with open('Popis_GO.txt', 'a', encoding='utf-8') as Fajl:
        for element in zaUFajl:
            Fajl.write(str(element) + '\n')
    return zaUFajl




    
with open('Popis_GO.txt', 'r', encoding='utf-8') as Fajl:
    
    redovi = Fajl.read() # čitanje u string
    
    aktualna = redovi.split('\n')
        


    
for i in range(len(aktualna)):
    aktualna[i] = aktualna[i][1 : -2]
    print(*aktualna[i], sep='')

# for i in range(len(aktualna)):
#     print(aktualna[i])
#     print()
    

    
print()
print(len(aktualna))
print()
print(aktualna[1][-1])
print()

aktualna[0].split()
print(aktualna[0][1])

    
# print()
# print(aktualna[0][0])
# print()
# print(type(aktualna[0][0]))

# prvaStavka = aktualna[0].split()

# print(prvaStavka[0])

print('\n##############')
print('\nKRAJ PROGRAMA\n')   
print('##############\n')