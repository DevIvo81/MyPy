import os, json
os.system('cls')
ulaznaLista = ['gorivo', 
            'smještaj',
            'cestarina', 
            'dnevni budžet', 
            'hrana', 
            'sadržaji']


def jeLiInteger(inputString):
    """Osigurava da je unesen
        cijeli broj i vraća
        unos kao int."""
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
    """
    while True:
        unos = input(inputString)
        try:
            unos = float(unos)
        except:
            print('\nGREŠKA, upiši broj, može i decimalni!')
            continue
        return unos
    
    
def pregledIDodavanjeStavke(ulaznaLista):
    
    print('\nTrenutni popis:\n')
    print('--------------------------------')
    print(*ulaznaLista, sep='\n')
    print
    
    if input('\nNova stavka? (D / N) --> ').lower() != 'd':
        
        print('\nU redu, popis troškova se ne mijenja.')
        
        return ulaznaLista
    
    else:      
        
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
        
        return ulaznaLista


def listaParovaZaDict(ulaznaListaStavki, inputString='Upiši cijenu za'):
          
    listaParova =[[ulaznaListaStavki[i], 

        jeLiInteger(f'\n{inputString} {ulaznaListaStavki[i]} --> ')] \

            for i in range(len(ulaznaListaStavki))]
    
    print('\n---------------------------')
    print('UNOS ZAVRŠEN')
    print('---------------------------')
    
    suma = 0
    
    for i in range(len(listaParova)):
        suma += listaParova[i][1]

    listaParova.append(['TOTAL', suma])
    
    return listaParova


def rjecnikStavki():
            
    parITotal = listaParovaZaDict(pregledIDodavanjeStavke(ulaznaLista))

    kazaloStavki = {}

    for i in range(len(parITotal)):
        kazaloStavki[parITotal[i][0]] = parITotal[i][1]

    return kazaloStavki



def GOPopis(kazaloGO = {}):

    if input('\nNova opcija? (D za dodavanje) --> ').lower() != 'd':
        print('\nDoviđenja!\n')
    else:
        
        brojOpcija = jeLiInteger('\nKoliko novih opcija? --> ')
        
        for i in range(brojOpcija):
            
            while True:
                
                odrediste = input('\nDestinacija? --> ').upper()
                
                if odrediste in kazaloGO.keys():
                    print('\nTa opcija već postoji!')
                    continue
                else:
                    
                    kazaloGO[odrediste] = rjecnikStavki()
                    break
        print('\nUNOS DESTINACIJA ZAVRŠEN\n')
    return kazaloGO
        


trenutneOpcije = GOPopis()

with open('POPIS.json', 'a', encoding='utf8') as addToFile:
    json.dump(trenutneOpcije, addToFile, ensure_ascii=False, indent=2)

with open('POPIS.json', 'r', encoding='utf8') as f:
    GODict = {k : v for k,v in json.load(f).items()}
    json.load(f)
    for k, v in GODict.items():    
        print(f'{k} {v}')




