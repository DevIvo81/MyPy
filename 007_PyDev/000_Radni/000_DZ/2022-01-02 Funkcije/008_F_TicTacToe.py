import os

os.system('cls')

print()

# VARIJABLE LISTI ZA TABELU

a = list("  7  |  8  |  9  ")
b = list("-----+-----+-----")
c = list("  4  |  5  |  6  ")
d = list("-----+-----+-----")
e = list("  1  |  2  |  3  ")


brojač = 0
prvi = 'X'
pokus = []
check = False


def tabela_1():

    a = list("  7  |  8  |  9  ")
    b = list("-----+-----+-----")
    c = list("  4  |  5  |  6  ")
    d = list("-----+-----+-----")
    e = list("  1  |  2  |  3  ")

    os.system('cls')
    print('\n#### ZAIGRAJMO KRIŽIĆ-KRUŽIĆ ####\n')
    print(*a)
    print(*b)
    print(*c) 
    print(*d) 
    print(*e)


def tabela():
    os.system('cls')
    print('\n#### ZAIGRAJMO KRIŽIĆ-KRUŽIĆ ####\n')
    print(*a)
    print(*b)
    print(*c) 
    print(*d) 
    print(*e) 
 

def provjera():
    
    global prvi, check
    
    for i in range(len(a)):
        
        if a[2] == prvi and a[8] == prvi and a[14] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif c[2] == prvi and c[8] == prvi and c[14] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif e[2] == prvi and e[8] == prvi and e[14] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif a[2] == prvi and c[2] == prvi and e[2] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif a[8] == prvi and c[8] == prvi and e[8] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif a[14] == prvi and c[14] == prvi and e[14] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif a[2] == prvi and c[8] == prvi and e[14] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break
        elif a[14] == prvi and c[8] == prvi and e[2] == prvi:
            print('\nIgrač ', prvi,' je pobjednik!')
            check = True
            break   
    return check
    
def TicTacToe():

    global brojač, prvi, pokus, check

    tabela_1()

    while True:
        
        if prvi == 'X':
            
            while True:
            
                znak = int(input('\nUnesi broj polja na koje želiš staviti "X": '))
                
                if znak in pokus:
                    tabela()
                    print('\nTo je već isprobano! Pokušaj ponovno!\n')
                else:
                    pokus.append(znak)
                    break
                                        
            for i in range(len(a)):
                if a[i] == str(znak):
                    a[i] = prvi
                if c[i] == str(znak):
                    c[i] = prvi
                if e[i] == str(znak):
                    e[i] = prvi
            tabela()        
        
        provjera()
        
        if check == True:
            break                         
        else:
            prvi = 'O'
            brojač += 1                    
            print('\nBrojač poteza - ', brojač)
        
        provjera()
        
        if brojač == 7 and check == False:
            tabela()
            print('\nBrojač poteza - ', brojač)
            print('\n####   NERIJEŠENO!   ####\n')
            break
        
        if prvi == 'O':
            
            while True:

                znak = int(input('\nUnesi broj polja na koje želiš staviti "O": '))
                
                if znak in pokus:                    
                    tabela()
                    print('\nTo je već isprobano! Pokušaj ponovno!\n')
                else:
                    pokus.append(znak)
                    break
                        
            for i in range(len(a)):
                if a[i] == str(znak):
                    a[i] = 'O'
                elif c[i] == str(znak):
                    c[i] = 'O'
                elif e[i] == str(znak):
                    e[i] = 'O'
            tabela()
        provjera()
        
        if check == True:            
            break             
        else:
            prvi = 'X'
            brojač += 1
            print('\nBrojač poteza - ', brojač)
    
        provjera()
        
        if brojač == 8 and check == False:
            tabela()
            print('\nBrojač poteza - ', brojač)
            print('\n####   NERIJEŠENO!   ####\n')
            break


while True:
    
    TicTacToe()
    
    if input('\nJoš jednu rundu? ["n" za izlaz] --> ').lower() == 'n':
        print('\nDo sljedećeg puta, pozdrav!\n')
        break
input()
    


    
    



