import os, random
os.system('cls')

# 4. KAMEN ŠKARE i PAPIR

baza = ['KAMEN', 'ŠKARE', 'PAPIR']

while True:
    
    zaP1 = 1
    zaP2 = 1

    while zaP1 < 3 and zaP2 < 3:
        
        p1 = random.choice(baza)
        p2 = random.choice(baza)
        
        if p1 == p2 and p2 == p1:
            print(f'\n{p1} == {p2} tak da nikom ništ...!')
        
        elif p1 == baza[0] and p2 == baza[1]:
            print(f'\nP1:{p1} lomi P2:{p2}')
            zaP1 += 1
        elif p2 == baza[0] and p1 == baza[1]:
            print(f'\nP2:{p2} lomi P1:{p1}')
            zaP2 += 1
        
        elif p1 == baza[1] and p2 == baza[2]:
            print(f'\nP1:{p1} režu P2:{p2}')
            zaP1 += 1
        elif p2 == baza[1] and p1 == baza[2]:
            print(f'\nP2:{p2} režu P1:{p1}')
            zaP2 += 1
        
        elif p1 == baza[2] and p2 == baza[0]:
            print(f'\nP1:{p1} omata P2:{p2}')
            zaP1 += 1
        elif p2 == baza[2] and p1 == baza[0]:
            print(f'\nP2:{p2} omata P1:{p1}')
            zaP2 += 1
        
    if zaP1 > zaP2:
        print(f'\nIgrač 1 je pobjednik sa {zaP1} : {zaP2}')
    else:
        print(f'\nIgrač 2 je pobjednik sa {zaP2} : {zaP1}')
    
    if input('\nNova igra? [N za prekid] --> ').upper() == 'N':
            print('\n Do sljedećeg puta, pozdrav!\n')
            break
