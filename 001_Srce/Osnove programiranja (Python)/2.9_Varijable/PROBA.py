import os
os.system('cls')

n = int(input("\nUnesi interval ispisa prostih brojeva:"))

for i in range(2,n):
    prim = True
    for j in range(2,i):
        if i % j == 0:
            prim = False
    if prim == True:
        print(i, end=' ')
    else:
        print(" ", end='')