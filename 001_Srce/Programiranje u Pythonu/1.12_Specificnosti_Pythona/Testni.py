import os
os.system('cls')

'''for i in range(2):
    print('\nHello World')
'''
# LISTA U OBRNUTOM PORETKU
'''
lista = [i for i in range(10)]
obr_lista = lista[::-1]
'''
''''
print('\nOriginalna lista:\n', lista)
print('\nObrnuta lista:\n', obr_lista)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('\nOrig lista: ', lista)
print('\nlista[2:5]: ', lista[2:5])
print()
print('\nOrig lista: ', lista)
print('\nlista[2]: ', lista[2])
print()
print('\nOrig lista: ', lista)
print('\nlista[:5]: ', lista[:5])
print()
print('\nOrig lista: ', lista)
print('\nlista[-1]: ', lista[-1])
print()
print('\nOrig lista: ', lista)
print('\nlista[-2:]: ', lista[-2:])
print()
print('\nOrig lista: ', lista)
print('\nlista[:-2]: ', lista[:-2])
print()
print('\nOrig lista: ', lista)
print('\nlista[::2]: ', lista[::2])
print()
print('\nOrig lista: ', lista)
print('\nlista[1:5:2]: ', lista[1:5:2])
print()
print('\nOrig lista: ', lista)
print('\nlista[::-2]: ', lista[::-2])
print()
print('\nOrig lista: ', lista)
print('\nlista[::-1]: ', lista[::-1])
print()
print('\nOrig lista: ', lista)
print('\nlista[1::-1]: ', lista[1::-1])
print()
print('\nOrig lista: ', lista)
print('\nlista[:-3:-1]: ', lista[:-3:-1])
print()
print('\nOrig lista: ', lista)
print('\nlista[-3::-1]: ', lista[-3::-1])
print()
'''
# NIZ ZNAKOVA (STRING) U OBRNUTOM PORETKU
'''
nizZnakova = 'abcdefghijkl'
obrnutiNizZnakova = nizZnakova[::-1]

print('\nOriginalni string: ', nizZnakova)
print('\nObrnuti string: ', obrnutiNizZnakova)
'''
# ZAMJENA VRIJEDNOSTI VARIJABLI U JEDNOJ LINIJI
'''
a = 10
b = 20
print(a, b)
print()
b, a = a, b
print(a, b) # raspakiravanje tuplea

x = 1, 2
a, b = x # a,b = (1,2) ; x je n-terac(tuple)
         # broj varijabli mora točno odgovarati
         # broju elemenata u n-tercu.
'''
# SPREMANJE VRIJEDNOSTI IZ VARIJABLE U LISTU
''''
lista = [1, 2, 3]

a, b, c = lista

print(a, b, c)
'''
# ULANČANI OPERATORI USPOREDBE
'''
a = 10
print(3<a<20)
print(10<a<20)
'''

# KONSTRUKCIJA for - else
# "else" dio petlje "for" se izvršava
# samo kada petlja "for" do kraja odradi
# svoj posao, bez prekida naredbom "break".
'''
lista = [i for i in range(1,6)]

# Kada je "for" petlja prekinuta naredbom
# "break", "else" dio se ne izvršava. U
# ovom slučaju element 5 postoji u listi.
for element in lista:
    if element == 5:
        break
else:
    print('Nije pronađeno')
# Ovdje element u "for" petlje nije
# pronađen pa se "else" dio izvršava.
for element in lista:
    if element == 0:
        break
else:
    print('Nije pronađeno!')
'''
'''
# TERNARNI OPERATOR
# omogućuje da se funkcionalnost "if-else"
# naredbe napiše u jednom retku

x = 10 if True else 20  
print(x)

x = 10 if False else 20
print(x)
'''
# POZIV FUNKCIJE POMOĆU TERNARNOG OPERATORA

# [istina] if [logički] else [lažni]
'''
def funPrva(vrijednost):
    print('funPrva(), vrijednost: ', vrijednost)

def funDruga(vrijednost):
    print('funDruga(), vrijednost: ', vrijednost)

x = True

(funPrva if not x else funDruga)(10)
'''

rijec = 'Srxce'

for e in rijec:
    if e == 'x':
        pass
    else:
        print(e, end=' ')




