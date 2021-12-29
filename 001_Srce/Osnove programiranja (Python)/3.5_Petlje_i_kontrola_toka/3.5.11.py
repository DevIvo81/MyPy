''''** Napišite program koji će inicijalizirati varijablu "n" na proizvoljnu 
cjelobrojnu vrijednost. Vrijednost varijable "n" neka predstavlja red tablice. 
Ispisati tablicu veličine n-redaka i n-stupaca. Vrijednost 1 
neka se nalazi na glavnoj dijagonali, a vrijednost 0 na svim ostalim 
mjestima. 
Primjer za n = 5:

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1

'''

import os
os.system('cls')

#n = 5
n = 7

#n = int(input("Unesi broj redaka/stupaca: "))

for y in range(1, n+1):
    for x in range(1, n+1):
        #print(x, end='  ')
        if y == x:
            print(1, end='  ')
        else:
            print("0", end='  ')
    print()
    print()
    