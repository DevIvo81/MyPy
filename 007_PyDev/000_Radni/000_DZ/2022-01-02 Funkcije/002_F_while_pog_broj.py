import os, random
os.system('cls')

# 2. POGAĐANJE BROJA

print('\nPOGAĐAMO NASUMIČNI BROJ [ 1 <--> 99]\n')


def funPogodataka():
        
    RANDOM_BROJ = random.randint(1, 99)
    
    brojac = 1
    
    while True:   
        
        UNOS = input('\nUpiši broj --> ')
        
        if UNOS.isalpha():
            print('\nTraži se cijeli broj, pokušaj ponovno!')
                
        else:
            
            UNOS = int(UNOS)
            
            if UNOS == RANDOM_BROJ:      
                print(f'\nBravo, {UNOS} je točan broj! Uspjeh u {brojac} pokušaja!\n')
                break
            
            if UNOS > RANDOM_BROJ:
                print(f'\nMANJI je od {UNOS}')          
            
            elif UNOS < RANDOM_BROJ:
                print(f'\nVEĆI je od {UNOS}')
            
            brojac += 1
    return ''

def igra():
           
    while True:
        
        funPogodataka()    
                
        if input('\nŽelite li pokušati ponovno (ENTER za prekid) --> ') == '':
            print()
            print('\nDo sljedećeg puta, pozdrav!\n')
            break
    return ''

igra()