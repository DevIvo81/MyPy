import os, random
os.system('cls')

# 4. LOTO 7 / 45

# Napravite LOTO 7/45 aplikaciju. U bubnju se nalazi 45 brojeva. 
# Korisnik treba odigrati 7 brojeva. Nakon odigranih brojeva 
# prikazuju se izvučeni i odigrani brojevi, broj pogodaka te 
# pogođeni brojevi. Svi brojevi se prikazuju sortirano. U 
# aplikaciji treba osigurati da korisnik ne može više 
# puta odigrati isti broj.

while True:

    # lista raspona brojeva
    bubanj = [i for i in range(1, 46)]

    jackpot = []
    # listu punimo sa 7 brojeva
    while len(jackpot) < 7:
        # generiranje dobitne kombinacije
        dobitni = random.choice(bubanj)
        # osiguranje da se nasumični brojevi ne ponavljaju
        if dobitni not in jackpot:
            jackpot.append(dobitni)
    jackpot.sort()

    srecka = []
    # upis brojeva u srećku
    brojac = 1
    # listu punimo sa 7 brojeva
    while len(srecka) < 7:
        
        os.system('cls')
        
        title = '   LOTO 7/45    '
        print(f'{ ( len(title) + 1 ) * "*" }'
            f'\n\n{ title }'
            f'\n\n{( len(title) + 1) * "*" }')
        
        srecka.sort()
        # prikaz dosad upisanih brojeva
        print('\nUpisani brojevi', *srecka, sep=' ')        
        
        broj = input(f'\nUpiši {brojac}. broj --> ')
        # osiguranje za unos slova
        if broj.isalpha():
            print( '\nUneseno je slovo! Pokušaj ponovno.' )
            input()
        else:
            
            broj = int(broj)
            # onemogućavanje ponavljanja brojeva
            if broj in srecka:    
                print( '\nBrojevi se ne smiju ponavljati! Pokušaj ponovno.' )
                input()
            elif not 1 <= broj <= 45:
                print( '\nBroj van raspona! Pokušaj ponovno.' )
                input()
            else:
                # ako je sve u redu    
                srecka.append(broj)
                brojac += 1

    pogodaci = 0

    for i in range(7):
        if srecka [i] in jackpot:
            pogodaci += 1    

    fond = 10000000

    print( f'\nDobitna kombinacija glasi\t{ jackpot }' )
    print( f'\nOdigrana je kombinacija\t\t{ srecka }' )

    if pogodaci == 3:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .003)} HRK')
    elif pogodaci == 4:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .009)} HRK')
    elif pogodaci == 5:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .07)} HRK')
    elif pogodaci == 6:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .13)} HRK')
    elif pogodaci == 7:
        print(f'\nBravo, {pogodaci} pogodataka! JACKPOT iznosi {round(fond * .46)} HRK')
    else:
        print(f'\nNažalost, svega {pogodaci} pogodataka! Više sreće drugi put\n')
    
    if input('\nNova srećka? [N za prekid] --> ').upper() == 'N':
            print('\n Do sljedećeg puta, pozdrav!\n')
            break