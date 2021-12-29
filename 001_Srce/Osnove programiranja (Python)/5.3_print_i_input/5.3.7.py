'''7.  ** Učitajte s tipkovnice varijablu niz intervala [3, 10]. Učitavanje 
ponavljati tako dugo dok se ne učita ispravna vrijednost. U slučaju 
neispravne vrijednosti ispisati obavijest da je vrijednost neispravna. 
Ispisati tablicu od nredaka i nstupaca. Format ispisa zaključiti na 
temelju primjera koji se nalazi u nastavku (n=10).
1   2   3   4   5   6   7   8   9  10 
    11  12  13  14  15  16  17  18  19
        20  21  22  23  24  25  26  27 
            28  29  30  31  32  33  34
                35  36  37  38  39  40 
                    41  42  43  44  45
                        46  47  48  49 
                            50  51  52
                                53  54 
                                    55'''
import os
os.system('cls')

while True:

    #n = input("\nUnesi broj redaka i stupaca za ispis iz intervala [3, 10]: ")
    n = 5
    
    #if n.isdigit() == False:
     #   print("\nTo je slovo, a traži se broj! Pokušaj ponovno!\n")
          
    if not 3<=int(n)<=10:
        print("\nBroj je izvan zadanog intervala! Pokušaj ponovno!\n")
    
    else:
        b = 1
        c = 1 
        
            print()
        for i in range(0, n):
            for j in range(0, n-1):
                
            for j in range(0, i+1):
                print('', end=' ')
                c += 1
            print()
            
        break