'''7.  Implementirajte funkciju prototipa rezultat(var1, var2), 
funkcija može primiti dvije vrijednosti. Tako kreirana funkcija 
neka u pozivajući dio programa vraća tri vrijednosti dobivene 
sljedećim aritmetičkim operacijama: var1*var2, var1+var2, 
10*var1+var2. U glavnom dijelu programa pozovite prethodno 
implementiranu funkciju te njene povratne vrijednosti spremite u 
tri zasebne varijable proizvoljnog imena i ispišite ih.'''
import os
os.system('cls')

def rezultat(x, y):
    a = x * y
    b = x + y
    c = 10*x + y
    return a, b, c

x = int(input('\nUpiši prvi broj: '))
y = int(input('\nUpiši prvi broj: '))

var_1, var_2, var_3 = rezultat(x,y)

print(f'\nRezultat vrši operacije {x} * {y}, {x} + {y} i 10*{x} + {y}')
print()
print(f'Za brojeve {x} i {y} rezultati su: {var_1} {var_2} {var_3}')


