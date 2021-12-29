'''
Zatražite od korisnika unos dva broja. 
Nakon unosa brojeva, ispišite: zbroj, razliku, umnožak, 
količnik (rezultat djeljnja), potenciranje te modulo 
unesenih brojeva
Svaka operacija treba biti ispisana u novom redu, 
a ispis treba imati uključene brojeve, 
znak računske operacije te rezultat.
PRIMJER ISPISA: 
5 + 8 = 13
5 - 8 = -3

NAPOMENA Za sada kod unosa neka kod prvog unosa drugi
broj NE bude 0 (nula), jer nije dopušteno dijeliti s nulom.
To svakako pokušajte napraviti, ali NE u prvom pokušaju.
'''

# ime = input('Molimo upisite Vase ime: ')
# print('Dobar dan ', ime, 'Kruno.', sep='')

a = input('Upisite broj a: ')
#print(type(a))
a = int(a)
#print(type(a))


# b = input('Upisite broj b: ')
b = float(input('Upisite broj b: '))
#print(type(b))


print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '//', b, '=', a // b)
print(a, '**', b, '=', a ** b)
print(a, '%', b, '=', a + b)
