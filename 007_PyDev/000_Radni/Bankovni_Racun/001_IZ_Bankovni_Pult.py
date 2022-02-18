import os
from datetime import datetime as dt


#region GLOBALNE VARIJABLE I FUNKCIJE ZA PROVJERU
      # UPISANIH BROJEVA

sredstva = 20000
transakcije = []
brojacTransakcija = 0

godina = dt.now().year


mjesec = dt.now().month

if mjesec < 10:
    mjesec = f'''0{mjesec}'''


dan = dt.now().day

if dan < 10:
    dan = f'''0{dan}'''


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
            print('\nGREŠKA, upiši broj [0 -> 4]!')
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


#region IZBORNIK

while True:
    
    os.system('cls')

    print('''
            DOBRO DOŠLI TRANSAKCIJSKI PULT
        
    Upišite broj za izbor:
    
    1 --> Prikaz stanja računa
    2 --> Prikaz transakcija
    3 --> Polog novca na račun
    4 --> Podizanje novca s računa
    0 --> Za izlaz s pulta
        ''')

    izborKorisnika = jeLiInteger('\nVaš izbor? --> ')

#endregion


#region PRIKAZ STANJA RAČUNA

    if izborKorisnika == 1:
        
        print(f'\nIznos sredstava na računu je {round(sredstva, 2)} HRK')
        input('\nENTER za nastavak')
        continue

#endregion


#region PROMET PO RAČUNU


    elif izborKorisnika == 2:
        
        print('\nTRANSAKCIJE:\n')
        print(*transakcije, sep='\n\n')
        input('\nENTER za nastavak')
        continue
    
#endregion


#region POLOG NOVCA NA RAČUN
    
    elif izborKorisnika == 3:
        # UPLATA
        while True:
        
            iznosUplate = jeLiFloat('\nUpišite iznos uplate --> ')
        
            if input('\nENTER za potvrdu unosa') != '':
                continue
            else:
                print('\nUNOS POTVRĐEN')
                sredstva += iznosUplate
                brojacTransakcija += 1
                
                if brojacTransakcija < 10:
                    racun = f'R - 0{brojacTransakcija} - {godina}/{mjesec}/{dan}'
                else:
                    racun = f'R - {brojacTransakcija}-/{godina}/{mjesec}/{dan}'

                transakcije.append([f'{racun}, UPLATA --> {iznosUplate} HRK'])
                print(f'\nNovi iznos na računu --> {round(sredstva, 2)} HRK')
        
            if input('\nNovi polog? (D / N) --> ').lower() == 'd':                
                continue
            else:
                input('\nIZLAZ')
                break
#endregion        


#region PODIZANJE NOVCA S RAČUNA

    elif izborKorisnika == 4:
        # ISPLATA
        while True:
            
            iznosIsplate = jeLiFloat('\nUpišite iznos koji želite podići s računa --> ')
        
            if iznosIsplate > sredstva:
                print('\nNedovoljan iznos na računu, pokušajte ponovno!')
                continue
            else:
                if input('\nDa li je upisani iznos ispravan? ("D" za potvrdu, ENTER za ponovni unos) --> ').lower() != 'd':
                    continue
                else:
                    print('\nUNOS POTVRĐEN')
                    sredstva -= iznosIsplate
                    brojacTransakcija += 1
                    
                    if brojacTransakcija < 10:
                        racun = f'R - 0{brojacTransakcija} - {godina}/{mjesec}/{dan}'
                    else:
                        racun = f'R - {brojacTransakcija}-/{godina}/{mjesec}/{dan}'

                    transakcije.append([f'{racun}, ISPLATA --> {iznosIsplate} HRK'])
                    print(f'\nNovi iznos na računu --> {round(sredstva, 2)} HRK')
            
                if input('\nNova isplata? (D / N) --> ') == 'd':
                    continue        
                else:
                    input('\nIZLAZ')
                    break

#endregion


#region IZLAZ ILI POGREŠAN UNOS STAVKE IZ IZBORNIKA

    elif izborKorisnika == 0:
        print('\nDOVIĐENJA I UGODAN OSTATAK DANA')
        break
    else:
        print('\nPogrešan unos, pokušajte ponovno.')
        input('\nENTER za povratak')
        continue
    
#endregion