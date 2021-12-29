'''3.  * Napišite program koji s tipkovnice učitava proizvoljni cijeli 
troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom 
je 121.'''

import os
os.system('cls')

istina = True 

while istina:
        
    a = input('\nUpiši troznamenkasti broj: ')
           
    if a[:].isdigit() == False:
        print('\nGREŠKA! Traže se brojevi, a ne slova! Pokušaj opet!')

    else:
        
        if len(a) != 3:
            print('\nGREŠKA! Traži se troznamenkasti broj! Pokušaj opet!')
       
        else:
            a = int(a)
            for i in range(a, 1000):
                lista_brojeva = list(str(i))
                palindromi = lista_brojeva.copy()
                palindromi.reverse()
            
                if lista_brojeva == palindromi:
                    print('\nSljedeći troznamenkasti palindrom je ', i)
                    istina = False
                    break
input()


    
    
        




