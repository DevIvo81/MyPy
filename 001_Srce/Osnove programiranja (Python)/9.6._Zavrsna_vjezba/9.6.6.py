'''6.  * Kreirajte 4 funkcije koje implementiraju operacije: zbrajanja, 
oduzimanja, množenja i dijeljenja dvaju brojeva koji se u funkciju 
prenose kao parametri. Najprije od korisnika tražite da odluči želi li 
raditi zbrajanje, oduzimanje, množenje, dijeljenje ili prekidanje 
izvršavanja programa, a nakon toga omogućite unos dviju vrijednosti 
nad kojima će se napraviti željena operacija. Ovaj postupak 
ponavljati tako dugo dok se ne unese vrijednost za prekidanje 
programa. U nastavku slijedi primjer:
Odaberite računsku operaciju:
1 – zbrajanje
2 – oduzimanje
3 – množenje
4 – dijeljenje
0 – izlaz iz programa
Unesite broj željene operacije: 1 (ovo unosi korisnik preko tipkovnice)
Unesite prvu vrijednost: 5 (ovo unosi korisnik preko tipkovnice)
Unesite drugu vrijednost: 10 (ovo unosi korisnik preko tipkovnice)
Rezultat: 15
{Nakon ispisa rezultata ovu sekvencu ponavljajte tako dugo dok korisnik 
ne unese 0}'''
import os
os.system('cls')

def zbr(a, b):
    return print('\na + b = ', a + b)

def odu(a, b):
    return print('\na - b = ', a - b)

def mno(a, b):
    return print('\na * b = ', a * b)

def dij(a, b):
    if b == 0:
        return print('\nDijeljenje s nulom!')
    return print('\na / b = ', a / b)



while True:
      
    print('\nOdaberite računsku operaciju:\n','1 – zbrajanje',
        '2 – oduzimanje','3 – množenje','4 – dijeljenje',
        '0 – izlaz iz programa', sep='\n')
    
    x = int(input('\nOdabir: '))

    if x < 0 or x > 4:
        print('\nNepoznata operacija!')
        continue
    if x == 0:
        print('\nIzlaz iz programa!')
        break

    a = int(input('\nUpiši prvi broj: '))
    b = int(input('\nUpiši drugi broj: '))  
    
    if x == 1:  
        zbr(a,b)
    elif x == 2:
        odu(a,b)
    elif x == 3:
        mno(a,b)
    elif x == 4:
        dij(a,b)