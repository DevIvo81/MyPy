import os
os.system('cls')

a = input('\nBroj: ')
a = int(a)
print()
start, end = -a, a

for i in range(start, end):
    if i < 0:
        print(i, end=' ')
