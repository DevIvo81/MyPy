import os, random

# 4. KAMEN ŠKARE i PAPIR

def kamenSkareIPapir():
    
    baza = ['KAMEN', 'ŠKARE', 'PAPIR']
    
    zaP1 = 0
    zaP2 = 0
    
    while zaP1 < 3 and zaP2 < 3:
        
        p1 = random.choice(baza)
        p2 = random.choice(baza)
        
        if p1 == p2 and p2 == p1:
            print(f'\n{p1} == {p2} tak da nikom ništ...!')
        
        elif p1 == baza[0] and p2 == baza[1]:
            zaP1 += 1
            print(f'\nP1:{p1} lomi P2:{p2}\t{zaP1} : {zaP2}')
            
        elif p2 == baza[0] and p1 == baza[1]:
            zaP2 += 1
            print(f'\nP2:{p2} lomi P1:{p1}\t{zaP1} : {zaP2}')
            
        
        elif p1 == baza[1] and p2 == baza[2]:
            zaP1 += 1
            print(f'\nP1:{p1} režu P2:{p2}\t{zaP1} : {zaP2}')
            
        elif p2 == baza[1] and p1 == baza[2]:
            zaP2 += 1
            print(f'\nP2:{p2} režu P1:{p1}\t{zaP1} : {zaP2}')
        
        elif p1 == baza[2] and p2 == baza[0]:
            zaP1 += 1
            print(f'\nP1:{p1} omata P2:{p2}\t{zaP1} : {zaP2}')
        
        elif p2 == baza[2] and p1 == baza[0]:
            zaP2 += 1
            print(f'\nP2:{p2} omata P1:{p1}\t{zaP1} : {zaP2}')
        
    if zaP1 > zaP2:
        print(f'\nIgrač 1 je pobjednik sa {zaP1} : {zaP2}')
    else:
        print(f'\nIgrač 2 je pobjednik sa {zaP1} : {zaP2}')
  
while True:
    
    os.system('cls')
    
    kamenSkareIPapir()
    
    if input('\nJoš jednu rundu ("n" za izlaz): --> ').lower() == 'n':
        print('\nPOZDRAV!!\n')
        break
    
