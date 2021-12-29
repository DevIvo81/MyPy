'''8. * Napišite program unutar kojeg će biti inicijalizirane dvije 
varijable proizvoljnog imena. U prvu varijablu spremite niz 
znakova: "Hello World!", a u drugu varijablu spremite listu 
sadržaja [1, 2, 3, 4]. Ispišite na ekran niz znakova i listu u obrnutom poretku na dva načina. Najprije vrijednosti ispišite 
pomoću petlje, a nakon toga vrijednosti ispišite na način koji je 
objašnjen u poglavlju 1.1. i 1.2.'''
import os
os.system('cls')

a = 'Hello World!'
print(a)
print()
b = [1, 2, 3, 4]
print(b)

print('\nObrnuti ispis pomoću "for" petlje\n')

for i in range(len(a)-1,-1,-1):
    print(a[i], end='')

print()
print()

for i in range(len(b)-1,-1,-1):    
    print(b[i], sep =' ', end='')
print()

print('\nObrnuti ispis pomoću "while" petlje\n')

i = len(a) - 1
while i >= 0:
    print(a[i], sep='', end='')
    i -= 1
print()
print()

i = len(b) - 1
while i >= 0:
    print(b[i], sep='', end='')
    i -= 1



print()
print(a[::-1])
print()
print(b[::-1])

