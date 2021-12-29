'''5.  * U glavnom programu učitajte proizvoljni cijeli broj s tipkovnice. 
Implementirajte funkciju izracun() koja će učitanu vrijednost 
dohvatiti preko globalne varijable, a rezultat se vraća pomoću 
return naredbe. Kao rezultat potrebno je vratiti zbroj svih brojeva 
od 0 do unesenog broja. Na primjer, ako je unesena vrijednost -5, 
tada funkcija mora vratiti zbroj brojeva: - 5 - 4 - 3 - 2 - 1 = -15, ako 
pak je unesena vrijednost 4, tada funkcija mora vratiti zbroj brojeva: 
4 + 3 + 2 + 1 = 10. Rezultat ispišite na zaslon.'''

import os
os.system('cls')


def izracun():
     
    rezultat = 0

    a = x
    
    if a < 0:
        for i in range(a, 0):
            rezultat -= i
            print(i, end=' ')
        return print('= -',rezultat)
    else:
        for i in range(1, a+1):
            rezultat += i
            print(i, end=' ')
        return print('=',rezultat)
           
    

  
x = input('\nUpiši broj: ')
x = int(x)

izracun()
input()