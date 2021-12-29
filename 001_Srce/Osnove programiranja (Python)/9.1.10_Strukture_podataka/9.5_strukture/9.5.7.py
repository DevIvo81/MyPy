'''7.  Napišite program koji učitava elemente liste s tipkovnice. 
Učitavanje prekinuti onoga trenutka kada korisnik unese broj 5. 

Nakon što je lista učitana, program mora zamijeniti prvi element s posljednjim, 
drugi element s pretposljednjim i tako redom.'''
import os
os.system('cls')

lista = []

while True:
        element = input('Upiši element liste: ')
                
        if element == '5':        
            print()
            lista.reverse()
            print('\nLista u obrnutom poretku: ', lista)
            break
        else:
            os.system('cls')
            lista.append(element)
            print(lista, '\n')