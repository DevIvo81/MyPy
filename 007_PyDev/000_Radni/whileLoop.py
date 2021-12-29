import os, random
os.system('cls')

n = 7  

for i in range(n):
    print(' ' * (n - i), end='')
    print('*', end='')
    print('*' * i, end='')
    print('*' * i)
    
for j in range(n // 2):
    print(' ' * ((n // 2) + 2), end='')
    print('*' * ((n // 2) + 2), end='')
    print()
''' 
n - i = 7 - 0 = 7
n - i = 7 - 1 = 6
n - i = 7 - 2 = 5
...
'''