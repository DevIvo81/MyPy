from os import system as ss
ss('cls')

LIMIT_INT = 5
LIMIT_FLOAT = 5.5



def provjeraUnosaPovratInteger(LIMIT_INT):
    
       
    while True:
        
        unos = input('\nUpiši broj veći od 5 --> ')
        
        if unos.isdigit() == False or unos ==' ':
            print('\nERROR...Upisano je slovo ili realni broj!')
            continue
        
        unos = int(unos)
        
        if unos < LIMIT_INT:
            print('\nPremalo...!')
            continue
        else:
            unos -= LIMIT_INT
            print(f'\n{unos} je tip {type(unos)}')
            break
    
    return unos

def provjeraUnosaPovratFloat(LIMIT_FLOAT):

    while True:
        
        unos = input('\nUpiši broj veći od 5.5 --> ')
        
        try:
            unos = float(unos)
        except:
            print('\nEeej, realni broj!')
            continue
        
        unos = float(unos)
        
        if unos < LIMIT_FLOAT:
            print('\nPremalo...!')
            continue
        else:
            unos -= LIMIT_FLOAT
            print(f'\n{unos} je tip {type(unos)}')
            break
    
    return unos


# inte = provjeraUnosaPovratInteger(LIMIT_INT)
# print(f'\nPovrat iz funkcije integer {inte}')


floa = provjeraUnosaPovratFloat(LIMIT_FLOAT)
print(f'\nPovrat iz funkcije float {round(floa,2)}')


