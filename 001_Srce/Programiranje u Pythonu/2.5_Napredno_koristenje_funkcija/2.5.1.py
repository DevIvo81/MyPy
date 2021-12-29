import os
os.system('cls')

def plus(x):
    
    if x <= 1:
        return 1
    else:
        return x + plus(x-1)
        
x = int(input('\nUpiši cijeli broj: '))
broj = plus(x)
print(f'Zbroj brojeva od 1 do {x} iznosi {broj}')
    
        