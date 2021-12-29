'''* Napišite program koji ispisuje koliko ima prostih brojeva između 
dva proizvoljna broja.'''

import os


while True:

    os.system('cls')

    print("\nDanas ispisujemo proste (prim) brojeve iz raspona koji Vi unesete!\n")

    a = input("\n\nUnesi početak raspona: ")
    b = input("\n\nUnesi kraj raspona: ")
    if a.isdigit() == False and b.isdigit() == False:
        print("\nBrojevi se traže, ne slova! Pokušaj ponovno!")
        
    else:   
        if int(a) >= int(b):
            print("\nPa tražimo raspon i proste brojeve između! Pokušaj ponovno!")
        else:
            a = int(a)
            b = int(b)
            print()
            for i in range(a, b+1):
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    print(i, end=' ')
    
    resetiraj = input("\n\nŽelite li pokušati ponovno? [Y/N]: ")
    if resetiraj.upper() =='N':
        break        
        
