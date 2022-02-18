import os, string
os.system('cls' if os.name =='nt' else 'clear')


#region GLOBALNE VARIJABLE

bazaKorisnika = {'Pero Perić' : '123%$&ovI55', 'Ana Anić' : '87675%$&ovI55'}

#endregion


#region NASLOV

print('# ' * (len('IDENTITY MANAGEMENT')//2))
print('IDENTITY MANAGEMENT')
print('Autor: Ivo Zelić')
print('# ' * (len('IDENTITY MANAGEMENT')//2))
print(f'''

Lozinka mora sadžavati:

- Najmanje 10, a najviše 16 znakova
- Barem jedno veliko slovo
- Barem jedan broj
- Barem jedan specijalni znak iz {string.punctuation}''')

#endregion


#region FUNKCIJE

def jeLiInteger(inputString):
      
      while True:
        unos = input(inputString)
        try:
            unos = int(unos)
        except:
            print('\nGREŠKA, upiši cijeli broj!')
            continue
        return unos


def unosIProvjeraLozinke():
    
    special = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    brojevi = '0123456789'
    velikaSlova = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    #region PROVJERA DULJINE

    while True:
        
        passWord = input('\nUpiši lozinku --> ')
        
        duljinaOK = False
        
        if len(passWord) <10:  
            print('\nPrekratka lozinka!')
            continue
            
        elif len(passWord) > 16:
            print('\nPreduga lozinka!')
            continue
        else:
            duljinaOK = True

    #endregion


    #region PROVJERA VELIKOG SLOVA
        
        postojiVeliko = False
        
        for znak in passWord:
            if znak in velikaSlova:
                postojiVeliko = True
                break
            
        if not postojiVeliko:

            print('\nFali veliko slovo!')
            continue
    #endregion       
                
        
    #region PROVJERA SPECIAL    
        
        postojiSpec = False
        
        for znak in passWord:
            if znak in special:
                postojiSpec = True
                break

        if not postojiSpec:
            print('\nFali specijalni znak!')
            continue

    #endregion


    #region PROVJERA broja
        
        postojibroj = False
        
        for znak in passWord:
            if znak in brojevi:
                postojibroj = True
                break

        if not postojibroj:
            print('fali broj!')
            continue
        
    #endregion
    
    
    #region KONAČNA PROVJERA
        
        if duljinaOK and postojibroj and postojiSpec:
            print('\nLozinka ispravna!')
            break
        else:
            continue
    
    return passWord

    #endregion


def unosKorisnika():

    global bazaKorisnika
    
    brojKorisnika = jeLiInteger('\nKoliko korisnika dodajemo? --> ')

    if brojKorisnika == 0:
        print('\nDrugi put.\n')
        return bazaKorisnika
    
    else:    
        
        for i in range(brojKorisnika):
            
            while True:
                ime = input('\nVaše ime? --> ').title()
                prezime = input('\nVaše prezime? --> ').title()
                
                if f'{ime} {prezime}'in bazaKorisnika.keys():
                    print('\nKorisnik već postoji!')
                    continue
                
                else:
                    lozinka = unosIProvjeraLozinke()
                    bazaKorisnika[f'{ime} {prezime}'] = lozinka
                    print(f'\nDobro došli, {ime} {prezime}')
                    break
        print('\nUNOS KORISNIKA ZAVRŠEN\n')
        return bazaKorisnika

#endregion


#region GLAVNI PROGRAM

def main():
    
    global bazaKorisnika
    
    print('\nTrenutno su u bazi sljedeći korisnici:\n')
    print(*bazaKorisnika.keys(), sep='\n')
    
    if input(f'\nNovi korisnik? (D za unos, ENTER za izlaz) --> ').lower() !='d':
        return print('\nDoviđenja!\n')
        
    else:
        bazaKorisnika = unosKorisnika()
        return print('\nKorisnici su:\n'), \
                print(*bazaKorisnika.keys(), sep='\n'),\
                    print('''
        #############
        KRAJ PROGRAMA
        #############
        
        
        ''')

main()
    
#endregion