import os
os.system('cls')
'''
# REKURZIVNE FUNKCIJE
# Funkcija koja poziva samu sebe

def faktorijel(x):
    if x <= 1:
        return 1
    else:
        return x * faktorijel(x-1)

rez = faktorijel(4)
print(rez)
'''
# BEZIMENE (LAMBDA) FUNKCIJE
# Za razliku od "def" funkcija, bezimene funkcije se definiraju
# korištenjem ključne riječi "lambda".
# lambda [argumenti] : izraz
# Količina argumenata je neograničena i međusobno se odijeljuju
# zarezom. Sintaksno je ograničena na samo jedan izraz.
# Ne može sadržavati petlje "for", "while", a ni uvjetne "if".
# Ograničenje se izbjegava ternarnim operatorom. Bezimena funkcija
# vraža izračunatu vrijednost bez ključne riječi "return"
'''
uvecajZa10 = lambda x: x + 10
# iako nemaju ime lambda funkciju se može spremiti u varijablu
print(uvecajZa10(5))
# Klasično
def uvecaj(x):
    return x + 10
print(uvecaj(5))

zbroji = lambda a, b, c: a + b + c
print(zbroji(1, 2, 3))
'''
# SLOŽENIJE KORIŠTENJE "filter()", "map()", "reduce()"

# filter(funkcija, iterable) argument funkcija 
# vraća True ili False za svaki pojedini element iz
# objekta iterable.

#filter() uklanja elemente s obzirom na zadani uvjet.
'''
lista = [1, 3, 4, 7, 11, 55, 100, 102, 104]
rez = list(filter(lambda e: (e % 2 == 0), lista))
print(rez)

# Klasično

def parnost(x):
    return x % 2 == 0

lista = [1, 3, 4, 7, 11, 55, 100, 102, 104]
rezultat = list(filter(parnost, lista))
print(rezultat)

def multipliciranje(n):
    return lambda a: a*n

dvaPuta = multipliciranje(2)
triPuta = multipliciranje(3)

print(dvaPuta(3))
print(triPuta(3))
'''
# UGNIJEŽĐENE FUNKCIJE:
'''
def vanjska():
    print('Vanjska funkcija.')

    def unutarnja():
        print('Unutarnja funkcija')
    
    unutarnja()

vanjska()

#####

def vanjska(x):
    print('Vanjska funkcija, x = ', x)

    def unutarnja(y):
        print('Unutarnja funkcija, y = ', y)
    unutarnja(x * 2)

vanjska(10)
'''
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
    
print("Fibonacci sekvenca: ")
for i in range(9):
    print(fibonacci(i))

def fib(n):
    def fibMemo(n, memo):
        if n in memo:
            return memo[n]

        fib = fibMemo(n-1, memo) + fibMemo(n-2, memo)
        memo[n] = fib
        print(memo)
        return fib

    memo = {1: 1, 2: 1}
    return fibMemo(n, memo)

print(fib(7))
print('---')
print(fib(7))
'''

# GENERATORSKE FUNKCIJE
# Kao rezultat vraćaju generator, tj iterabilni objekt.
# Koriste ključnu riječ "yield" umjesto "return"
# Otpuštaju vrijednosti više puta
# Vraćaju generator
'''
def generatorska(x):
    while x > 0:
        yield x
        x -= 1

g = generatorska(3)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
def generatorska(vrijednost):
    i = 0
    while i < vrijednost:
        yield i
        i += 1

g = generatorska(4)
for e in g:
    print(e)
print()

g = generatorska(4)
print(list(g))
print()

g = generatorska(4)

for e in g:
    print(e)
print (f'Broj elemenata: {len(list(g))}')


