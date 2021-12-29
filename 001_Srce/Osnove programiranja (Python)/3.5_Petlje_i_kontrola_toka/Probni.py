import os
os.system('cls')

retci = int(input("\nUnesi broj redaka: "))

# vanjska petlja
for i in range(1, retci+1): # unos broja redaka
    # unutarnja petlja
    for j in range(1, i+1): # unos broja stupaca
        print('*', end=' ') # ispiši "*" koliki je broj retka s razmakom " ".
    print() # kad završiš sa ispisom prijeđi u novi red.

for i in range(3):
    for j in range(5):
        print("*", end=' ')
    print()



