import os, random
os.system('cls')

# 4. LOTO 7 / 45

# Napravite LOTO 7/45 aplikaciju. U bubnju se nalazi 45 brojeva. 
# Korisnik treba odigrati 7 brojeva. Nakon odigranih brojeva 
# prikazuju se izvučeni i odigrani brojevi, broj pogodaka te 
# pogođeni brojevi. Svi brojevi se prikazuju sortirano. U 
# aplikaciji treba osigurati da korisnik ne može više 
# puta odigrati isti broj.


# Kreiranje dobitne kombinacije
def Jackpot():

    # Lista raspona brojeva
    bubanj = [i for i in range(1, 46)]
    
    # Jackpot počinje kao prazna lista
    jackpot = []
    
    # Listu punimo sa 7 brojeva
    while len(jackpot) < 7:
        
        # Generiranje dobitne kombinacije
        dobitni = random.choice(bubanj)
        
        # Ako se nasumični brojevi ne ponavljaju
        # broj se dodaje u jackpot listu
        if dobitni not in jackpot:
            jackpot.append(dobitni)            
            # Sortiramo listu
            jackpot.sort()
    
    # Vraćamo sortiranu jackpot listu 
    return jackpot


# Korisnička kombinacija 
def Srecka():   
      
    # Srećka počinje kao prazna lista
    srecka = []
    
    # Brojač rednog broja upisa
    brojac = 1
           
    # Korisnik u listu "srecka" upisuje sa 7 brojeva        
    while len(srecka) < 7:
        
        os.system('cls')
        
        title = '   LOTO 7/45    '
        
        print(f'{(len(title) + 3) * "*"}\
             \n*{len(title) * " "} *\
            \n* {title}*\
            \n*{len(title) * " "} *\
            \n{(len(title) + 3) * "*"}')
                    
        # Prikaz dosad upisanih brojeva kao raspakirane liste
        print('\nUpisani brojevi', *srecka, sep=' ')        
        
        broj = input(f'\nUpiši {brojac}. broj --> ')               
        
        # Za slučaj da nije upisan broj
        if broj.isdigit() == False or broj == '':
            print( '\nUneseno je slovo! Pokušaj ponovno.' )
            input()
            
        else:            
            broj = int(broj)
            
            # Za slučaj upisa istog broja
            if broj in srecka:    
                print( '\nBrojevi se ne smiju ponavljati! Pokušaj ponovno.' )
                input()
            
            # Za slučaj da je broj van dopuštenog raspona 1-45
            elif not 1 <= broj <= 45:
                print( '\nBroj van raspona! Pokušaj ponovno.' )
                input()
            
            # Ako je sve u redu    
            else:
                srecka.append(broj)
                
                # Sortiramo listu
                srecka.sort()
                
                brojac += 1
    
    # Vraćamo sortiranu srecka listu 
    return srecka


# CHEAT MODE
def sreckaCheat(jackpotCheat):
        
    # Srećka počinje kao prazna lista
    srecka = []
    
    # Brojač rednog broja upisa
    brojac = 1
           
    # Korisnik u listu "srecka" upisuje sa 7 brojeva    
    
    while len(srecka) < 7:
        
        os.system('cls')
        
        title = '   LOTO 7/45    '
        
        print(f'{(len(title) + 3) * "*"}\
             \n*{len(title) * " "} *\
            \n* {title}*\
            \n*{len(title) * " "} *\
            \n{(len(title) + 3) * "*"}')
        # ISPIS ZA PROVJERU aka VARANJE...:)
        print(f'!!! SPOILER !!! {jackpotCheat} !!! CHEATER !!!')            
        # Prikaz dosad upisanih brojeva kao raspakirane liste
        print('\nUpisani brojevi', *srecka, sep=' ')        
        
        broj = input(f'\nUpiši {brojac}. broj --> ')               
        
        # Za slučaj da nije upisan broj
        if broj.isdigit() == False or broj == '':
            print( '\nUneseno je slovo! Pokušaj ponovno.' )
            input()
            
        else:            
            broj = int(broj)
            
            # Za slučaj upisa istog broja
            if broj in srecka:    
                print( '\nBrojevi se ne smiju ponavljati! Pokušaj ponovno.' )
                input()
            
            # Za slučaj da je broj van dopuštenog raspona 1-45
            elif not 1 <= broj <= 45:
                print( '\nBroj van raspona! Pokušaj ponovno.' )
                input()
            
            # Ako je sve u redu    
            else:
                srecka.append(broj)
                
                # Sortiramo listu
                srecka.sort()
                
                brojac += 1
    
    # Vraćamo sortiranu srecka listu 
    return srecka
        

# Provjera kombinacije
def loto7Od45():
    
    jackpot = Jackpot()
      
    if input('\nHOĆEŠ VARAT I SPOILAT (upiši "da" ako baš moraš)? --> ').lower() == 'da':
        srecka = sreckaCheat(jackpot)        
    else: 
        srecka = Srecka()
    
    pogodaci = 0
        
    for i in range(7):
        if srecka [i] in jackpot:
            pogodaci += 1    

    fond = 10000000

    print( f'\nDobitna kombinacija glasi\t{ jackpot }' )
    print( f'\nOdigrana je kombinacija\t\t{ srecka }' )

    if pogodaci == 3:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .0003)} HRK')
    elif pogodaci == 4:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .0009)} HRK')
    elif pogodaci == 5:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .007)} HRK')
    elif pogodaci == 6:
        print(f'\nZa {pogodaci} pogodatka nagrada je {round(fond * .13)} HRK')
    elif pogodaci == 7:
        print(f'\nBravo, {pogodaci} pogodataka! JACKPOT iznosi {round(fond * .46)} HRK')
    else:
        print(f'\nNažalost, svega {pogodaci} pogodataka! Više sreće drugi put\n')



# Glavni program 
while True:
        
    loto7Od45()
     
    if input('\nNova srećka? [N za prekid] --> ').upper() == 'N':
                print('\n Do sljedećeg puta, pozdrav!\n')
                break