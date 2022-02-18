#  AUTOMAT ZA NAPLATU PARKIRANJA


# Perfekcionizam u ispisu
def infoPult(brojSati, ukupnaCijena):
    
    import os
    
    os.system('cls')

    info = (f'''
********************************
*                              *
*  CIJENA PARKIRANJA - 6 KN/h  *
*                              *
********************************
Dobar dan. Vaše parkiranje je 
trajalo {brojSati} sati, što 
ukupno iznosi {ukupnaCijena} HRK
''')
    
    while True:
        if brojSati == 1:
            noviInfo = info[ : 210] + info[211 : ]
            break
        elif brojSati == 2 or brojSati == 3 or brojSati == 4:
            noviInfo = info[ : 210] + 'a' + info[211 : ]
            break
        else: 
            noviInfo = info
            break

    print(noviInfo)


# Za slučaj unosa slova
def provjeraTipaUnosa(unos):      
        
    if unos.isdigit() == False or unos == '':
        print(f'\nPokušajte ponovno brojkama, a ne slovima. ENTER za nastavak')
        input()
    else:
        return int(unos)

# Račun kusura    
def izracunRazlike(provjereniUnos, cijena):            
              
    if provjereniUnos >= cijena:
        razlika = provjereniUnos - cijena
        print(f'\nIznos za povrat je {razlika} HRK\n')
        return razlika
    else:
        print(f'\nMalo fali... [ENTER za ponovni unos]!')
        input()

# Procesuiranje naplate
def stroj(brojKuna):
    
    while brojKuna >= 0:
                            
        if brojKuna == 0:
            print('\nHvala!')
            break
        
        if (brojKuna - 5) >= 0:
            print('Vraćam kovanicu od 5 kuna')
            brojKuna -= 5
            
        else:
            if (brojKuna - 2) >= 0:
                print('Vraćam kovanicu od 2 kune')
                brojKuna -= 2
            else:
                print('Vraćam kovanicu od 1 kune')
                brojKuna -= 1
    
    return brojKuna

# Sve u jednom
def automatZaNaplatu():
    
    from random import randint as rint
    
    vrijemeParkiranja = rint(1,6)  # Da za svaku kartu bude drugačija naplata
    cijenaParkiranja = vrijemeParkiranja * 6

    while True:      
        
        infoPult(vrijemeParkiranja, cijenaParkiranja)
        
        iznos = input('\nKoliko HRK ste ubacili? --> ')
        
        provjeraUnosa = provjeraTipaUnosa(iznos)
                
        if provjeraUnosa != None:  # Da ne preskoči ako je unos 0
            
            povrat = izracunRazlike(provjeraUnosa, cijenaParkiranja)            
            
            if povrat != None:   
                naplata = stroj(povrat)
                if naplata >= 0:    # I opet...
                    break

# Glavni program
while True:
    
    automatZaNaplatu()
    
    if input('\nJoš jedna karta? ["0" za izlaz] --> ') == '0':
        print('\nDo sljedećeg puta, pozdrav!\n')
        break