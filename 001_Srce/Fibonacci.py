# Fibonacci array 0 -> 50

import os
os.system('cls')

x, y = 0, 1

while y < 50:
    print(y, end=' ')
    x, y = y, y + x
    

nlength = int(input('\nEnter the series length '))

a, b, c = 0, 1, 0
count = 0

if nlength <= 0:
    print('\nPlease enter positive integer!')
elif nlength == 1:
    print(f'\nFibonacci sequence up to {nlength}: {a}')
else:
    print(f'\nFibonacci sequence:')
    while c < 56:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        count += 1

    
    
    