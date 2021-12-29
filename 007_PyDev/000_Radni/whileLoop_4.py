import os, random
os.system('cls')

print('\nPOGAĐAMO NASUMIČNI BROJ [ 1 --> 99]\n')

broj = random.randint(1, 99)
brojac = 0

while True:
    
    n = int(input('\nUpiši broj --> '))
    brojac += 1
    
    if n == broj:      
        print(f'\nBravo, {n} je točan broj! Uspio si u {brojac} pokušaja.')
        if input('\nŽelite li pokušati ponovno (N za prekid)').upper() == 'N':
            print('\n Do sljedećeg puta, pozdrav!\n')
            break

    if n > broj:
        print(f'\nMANJI je od {n}')
        
    elif n < broj:
        print(f'\nVEĆI je od {n}')

        
