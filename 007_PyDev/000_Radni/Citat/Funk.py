import os
os.system('cls' if os.name =='nt' else 'clear')

def jeLiInteger(inputString):
    """Osigurava da je unesen
        cijeli broj i vraća
        unos kao int.
    Args:
        inputString ([str]): ['User TODO']
    """
    while True:
        unos = input(inputString)
        try:
            unos = int(unos)
        except:
            print('\nGREŠKA, upiši cijeli broj!')
            continue
        return unos


def jeLiFloat(inputString):
    """Osigurava da je unesen
        decimalni broj i vraća
        unos kao float.
    Args:
        inputString ([str]): ['User TODO']
    """
    while True:
        unos = input(inputString)
        try:
            unos = float(unos)
        except:
            print('\nGREŠKA, upiši broj, može i decimalni!')
            continue
        return unos


def upisNoveStavke(ulaznaLista):
    
    brojStavki = jeLiInteger('\nKoliko novih stavki --> ')
    
    for i in range(brojStavki):
        
        while True:
                    
            upis = input('\nUpiši novu stavku --> ')
            
            if upis in ulaznaLista:
                print('\nStavka već postoji, pokušaj opet.')
                continue
            
            else:
                ulaznaLista.append(upis)
                break
    
    print('\n---------------------------')
    print('UNOS STAVKI ZAVRŠEN')
    print('---------------------------')
    
    return ulaznaLista


def obradaListeTroškova():
    
    ulaznaLista = ['gorivo', 
            'smještaj']
            # 'cestarina', 
            # 'dnevni budžet', 
            # 'hrana', 
            # 'sadržaji']
    
    print('\nTrenutni popis troškova:\n')
    print('--------------------------------')
    print(*ulaznaLista, sep='\n')
    print
    
    if input('\nNovi trošak? (D / N) --> ').lower() != 'd':
        
        print('\nU redu, popis troškova se ne mijenja.')
        
        return ulaznaLista
    
    else:      
        return upisNoveStavke(ulaznaLista)









def listaParovaZaDict(ulaznaLista, inputString='Upiši vrijednost koja se traži'):
          
    listaParova =[[ulaznaLista[i], 

        jeLiInteger(f'\n{inputString} {ulaznaLista[i]} --> ')] \

            for i in range(len(ulaznaLista))]
    
    print('\n---------------------------')
    print('UNOS ZAVRŠEN')
    print('---------------------------')
    
    suma = 0
    
    for i in range(len(listaParova)):
        suma += listaParova[i][1]

    listaParova.append(['TOTAL', suma])
    
    return listaParova
    









def dodajTOTAL(listaParova):
    
    suma = 0
    
    for i in range(len(listaParova)):
        suma += listaParova[i][1]

    listaParova.append(['TOTAL', suma])
    
    return listaParova


#popisITotalJedneOpcije = dodajTOTAL(listaParova)




def listaOpcija(ulaznaLista):
    
    popisOpcija = []
        
    brojOpcija = jeLiInteger('\nKoliko novih opcija --> ')

    for i in range(brojOpcija):
    
        upis = input(f'\nUpiši novu opciju --> ')
        
        popisOpcija.append([upis, ulaznaLista])
        
    print('\n---------------------------')
    print('UNOS OPCIJA ZAVRŠEN')
    print('---------------------------')

    return popisOpcija

# opcija = listaOpcija(popisITotalJedneOpcije)
# print('\nJEDNA OPCIJA\n')
# print(*opcija, sep='\n\n')