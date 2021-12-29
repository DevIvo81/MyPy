'''
ZAD1
Napišite program koji korisniku omogućuje operacije: 
zbrajanje, oduzimanje, mnozenje, dijeljenje te modulo.

Neka korisnik upiše operaciju koju želi, 
neka upiše potrebne vrijednosti (ovisno o operaciji), 
a vi izračunajte te ispišite rezultat

ZAD2
Napišite program koji s tipkovnice učitava cijeli broj A, 
te ispisuje dva zrcalna pravokutna trokuta od A redaka, 
razmaknuta točno jednim razmakom. 

Primjer za A = 7:
******* *******
 ****** ******
  ***** *****
   **** ****
    *** ***
     ** **
      * *
'''

n = 7
for i in range(0, n):
    print(' ' * i, end='')
    print('*' * (n - i), end='')
    print(' ', end='')
    print('*' * (n - i))

    #print() # Za prelazak u novi red

'''
n - i = 7 - 0 = 7
n - i = 7 - 1 = 6
n - i = 7 - 2 = 5
...
'''
print('\n\n')

n = 7
for i in range(0, n):
    print(' ' * (n - i), end='')
    print('*', end='')
    print('*' * i, end='')
    print('*' * i)


for j in range((n // 2) - 1):
    print(' ' * ((n // 2) + 2), end='')
    print('*' * ((n // 2) + 2))