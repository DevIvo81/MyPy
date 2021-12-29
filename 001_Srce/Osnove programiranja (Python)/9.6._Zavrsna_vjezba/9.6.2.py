'''2.  * Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova 
spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju 
ista slova neovisno o veličini ('a' i 'A' tretirati jednako).'''

import os
os.system('cls')

prvi_niz = 'Rumpelštilskij'
drugi_niz = 'Čiribućiriba'
for i in range(len(prvi_niz)):
    for j in range(len(drugi_niz)):
        if prvi_niz[i].upper() == drugi_niz[j].upper():
            print(prvi_niz[i], ' == ', drugi_niz[j], ' na indeksu ', i, ' i ', j)
        
input()


