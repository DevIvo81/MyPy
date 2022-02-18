import os
from datetime import datetime as dt


#region GLOBALNE VARIJABLE

# korisnik = { }
korisnik = {'Ivo': ['Adresa: PYSPACE 2', 'Sjedište: ZAGREB', 'Poštanski broj: 10000', 'OIB: 06645556767']}

brojacKorisnika = 0
bazaKorisnika = {brojacKorisnika : korisnik}

eurValuta = ' EUR'
hrkValuta = ' HRK'

EURSredstva = 4765.42
HRKSredstva = 8864.21

transakcije = []
brojacTransakcija = 0

godina = dt.now().year

mjesec = dt.now().month
if mjesec < 10:
    mjesec = f'''0{mjesec}'''

dan = dt.now().day
if dan < 10:
    dan = f'''0{dan}'''

#endregion


#region FUNKCIJE ZA PROVJERU UPISANIH BROJEVA

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
            print('\nGREŠKA, upiši broj [0 -> 5]!')
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

#endregion


def noviKorisnik():   
    
    global korisnik
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    podaci = []
    imeTvrtke = input('\nIme tvrtke: ')
    podaci.append(f'Naziv: {imeTvrtke.upper()}')
    adresaTvrtke = input('\nUlica i broj tvrtke: ')
    podaci.append(f'Adresa: {adresaTvrtke.upper()}')
    sjedisteTvrtke = input('\nSjedište tvrtke: ')
    podaci.append(f'Sjedište: {sjedisteTvrtke.upper()}')
    postanskiBroj = input('\nPoštanski broj tvrtke: ')
    podaci.append(f'Poštanski broj: {postanskiBroj}')
    
    while True:
        
        OIBTvrtke = input('\nOIB (11 znamenki): ')
        
        if len(OIBTvrtke) != 11 or OIBTvrtke.isdigit() == False:
            input('\nNetočan unos OIB-a. ENTER za ponovni pokušaj.')
            continue
        else:    
            podaci.append(f'OIB: {OIBTvrtke}')
            break
    
    korisnik[imeTvrtke] = podaci
    input('\nKREIRAN NOVI KORISNIK')
    return korisnik


def ispisStanja(sredstva, valuta):
    
    global korisnik
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for k, v in korisnik.items():
        print(k)
        print(*v, sep='\n')
    
    print(f'''
    Iznos sredstava na računu:

    {round(sredstva, 2)}{valuta}
    
        ''')
  
    
#region IZBORNIK I GLAVNI PROGRAM

def izbornik():
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
    |-------------------------------------------|
    |      DOBRO DOŠLI u PyIZ TRANSAKCIJE       |
    |                                           |
    |             GLAVNI IZBORNIK               |
    |-------------------------------------------|
    |         Upišite broj za izbor:            |
    |                                           |
    |       1 --> Kreiranje računa              |
    |       2 --> Prikaz stanja računa          |
    |       3 --> Prikaz transakcija            |
    |       4 --> Polog novca na račun          |
    |       5 --> Podizanje novca s računa      |
    |       0 --> Za izlaz                      |
    |-------------------------------------------|
    ''')
    

while True:
    
    izbornik()
    
    if not korisnik:
        input('\nNOVI KORISNIK - ENTER za kreiranje korisničkog računa\n')
        korisnik = noviKorisnik()
        brojacKorisnika += 1
        if brojacKorisnika not in bazaKorisnika.keys(): 
            bazaKorisnika[f'{brojacKorisnika}'] = korisnik
        continue
    
    else:
        izborKorisnika = jeLiInteger('\nVaš izbor? --> ')

#endregion


#region KREIRANJE NOVOG RAČUNA
     
    if izborKorisnika == 1:
        noviKorisnik()
        
#endregion


#region PRIKAZ STANJA RAČUNA

    elif izborKorisnika == 2:
        
        while True:
            
            if input('\nOdaberite valutu (EUR / HRK) --> ').lower() == 'eur':    
                print()
                ispisStanja(EURSredstva, eurValuta)
                
            else:
                print()
                ispisStanja(HRKSredstva, hrkValuta)
            
            if input('\nNovi prikaz stanja ("DA" za novi, ENTER za izlaz) --> ').lower() == 'da':
                input('\nENTER za novi prikaz')
                continue
            else:
                input('\nENTER za povratak glavni izbornik')   
                break

#endregion


#region PROMET PO RAČUNU

    elif izborKorisnika == 3:
        
        print('\nTRANSAKCIJE:\n')
        print(*transakcije, sep='\n\n')
        input('\nENTER za povratak na glavni izbornik')
        continue
    
#endregion


#region POLOG NOVCA NA RAČUN
    
    elif izborKorisnika == 4:
        # UPLATA
        
        def uplata(sredstva, valuta):
        
            global brojacTransakcija, transakcije
            
            while True:
            
                ispisStanja(sredstva, valuta)
                
                iznosUplate = jeLiFloat('\nUpišite iznos uplate --> ')
            
                if input('\nENTER za potvrdu unosa') != '':
                    continue
                else:
                    print('\nUNOS POTVRĐEN')
                    
                    
                    sredstva += iznosUplate
                    brojacTransakcija += 1
                    
                    ispisStanja(sredstva, valuta)
                    
                    if brojacTransakcija  < 10:
                        racun = f'TR-{godina}/{mjesec}/{dan}--0000{brojacTransakcija}'
                    elif 10 <= brojacTransakcija < 100:
                        racun = f'TR-{godina}/{mjesec}/{dan}--000{brojacTransakcija}'
                    elif 100 <= brojacTransakcija  < 1000:
                        racun = f'TR-{godina}/{mjesec}/{dan}--00{brojacTransakcija}'
                    elif 1000 <= brojacTransakcija  < 10000:
                        racun = f'TR-{godina}/{mjesec}/{dan}--0{brojacTransakcija}'
                    else:
                        racun = f'TR-{godina}/{mjesec}/{dan}-{brojacTransakcija}'
                    
                    transakcije.append([f'{racun}, UPLATA --> {iznosUplate}{valuta}'])
                    
                    print(f'\nTRANSAKCIJA -- {racun} JE IZVRŠENA')
                
                    print(f'\nNovi iznos na računu --> {round(sredstva, 2)}{valuta}')
            
                if input('\nNovi polog? (D / N) --> ').lower() == 'd':                
                    continue
                else:
                    input('\nENTER za izlaz\n')
                    break
            
            return sredstva
        
        if input('\nOdaberite valutu (EUR / HRK) --> ').lower() == 'eur':    
            EURSredstva = uplata(EURSredstva, eurValuta)
        else:
            HRKSredstva = uplata(HRKSredstva, hrkValuta)

#endregion        


#region PODIZANJE NOVCA S RAČUNA

    elif izborKorisnika == 5:
    
        def isplata(sredstva, valuta):
            
            global brojacTransakcija, transakcije
            
            while True:
                
                ispisStanja(sredstva, valuta)
                
                iznosIsplate = jeLiFloat('\nUpišite iznos koji želite podići s računa --> ')
            
                if iznosIsplate > sredstva:
                    print('\nNedovoljan iznos na računu, pokušajte ponovno!\n')
                    continue
                else:
                    if input('\nDa li je upisani iznos ispravan? (ENTER za potvrdu) --> ') != '':
                        continue
                    
                    else:
                        input('\nENTER za isplatu.')
                        sredstva -= iznosIsplate
                        brojacTransakcija += 1
                        
                        ispisStanja(sredstva, valuta)
                        
                        if brojacTransakcija  < 10:
                            racun = f'TR-{godina}/{mjesec}/{dan}--000{brojacTransakcija}'
                        elif 10 <= brojacTransakcija < 100:
                            racun = f'TR-{godina}/{mjesec}/{dan}--00{brojacTransakcija}'
                        elif 100 <= brojacTransakcija  < 1000:
                            racun = f'TR-{godina}/{mjesec}/{dan}--0{brojacTransakcija}'
                        elif 1000 <= brojacTransakcija  < 10000:
                            racun = f'TR-{godina}/{mjesec}/{dan}--{brojacTransakcija}'
                        else:
                            racun = f'TR-{godina}/{mjesec}/{dan}-{brojacTransakcija}'

                        transakcije.append([f'{racun}, ISPLATA --> {iznosIsplate}{valuta}'])
                        
                        print(f'\nTRANSAKCIJA -- {racun} JE IZVRŠENA')
                        
                        print(f'\nNovi iznos na računu --> {round(sredstva, 2)}{valuta}')
                
                    if input('\nNova isplata? (D / N) --> ') == 'd':
                        continue
                    else:
                        input('\nENTER za izlaz\n')
                        break
            
            return sredstva       
        
        if input('\nOdaberite valutu (EUR / HRK) --> ').lower() == 'eur':    
            EURSredstva = isplata(EURSredstva, eurValuta)
        else:
            HRKSredstva = isplata(HRKSredstva, hrkValuta)

#endregion


#region IZLAZ ILI POGREŠAN UNOS STAVKE IZ IZBORNIKA

    elif izborKorisnika == 0:
        print('\nDOVIĐENJA I UGODAN OSTATAK DANA\n')
        break
    else:
        print('\nPogrešan unos, pokušajte ponovno.')
        input('\nENTER za povratak')
        continue
    
#endregion