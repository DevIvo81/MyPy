'''** Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x 
(stupac) i y(redak) neka budu manje od 10. Program neka ispiše 
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija 
je vrijednost "X".
Primjer: T=(1,1) 
---------- 
-X--------
----------
----------
----------
----------
----------
----------
----------
----------'''
import os
os.system('cls')

x = int(input("\nUnesi koordinatu 'X': "))
y = int(input("\nUnesi koordinatu 'Y': "))

print("\nKoordinate (x,y) daju točku X[", x,", ", y, "]\n")

for i in range(11): # po koordinati "Y"
    for j in range(11): # po koordinati "X"
        if j == x and i == y:
            print("X", end=' ')
        else:
            print("-", end=' ')
    print()
