'''1. Napravite 2 skupa podataka i napunite ih proizvoljnim vrijednostima 
te nakon toga napravite uniju i presjek tih skupova te ispišite rezultat 
i za uniju i za presjek.'''
import os
os.system('cls')

# UNIJA metoda "union()" ili operator "|"

skup1= {1, 5, 1, 5, 4, 7, 8, 2, 3, 2} 
skup2 = {1, 2, 3, 6}

print('\nSkup 1:')
print('\n', skup1)

print('\nSkup 2:')
print('\n', skup2)

print('\nUnija sa metodom "union()":')
print('\n', skup1.union(skup2))

print('\nUnija sa operatorom "|":')
print('\n', skup1 | skup2)

# PRESJEK metoda "intersection()" ili operator "&"

skup1= {1, 5, 1, 5, 4, 7, 8, 2, 3, 2} 
skup2 = {1, 2, 3, 6}

print('\nSkup 1:')
print('\n', skup1)

print('\nSkup 2:')
print('\n', skup2)

print('\nPresjek s metodom "intersection()":')
print('\n', skup1.intersection(skup2))

print('\nPresjek s operatorom "&":')
print('\n', skup1 & skup2)

# SKUPOVNA RAZLIKA metoda "difference()" ili operator "-"

skup1= {1, 5, 1, 5, 4, 7, 8, 2, 3, 2} 
skup2 = {1, 2, 3, 6}

print('\nSkup 1:')
print('\n', skup1)

print('\nSkup 2:')
print('\n', skup2)

print('\nSkupovna razlika s metodom "difference()":')
print('\n', skup1.difference(skup2))
print('\n', skup2.difference(skup1))

print('\nSkupovna razlika s operatorom "-":')
print('\n', skup1 - skup2)
print('\n', skup2 - skup1)

# PRESJEK metoda "intersection()" ili operator "&"

skup1= {1, 5, 1, 5, 4, 7, 8, 2, 3, 2} 
skup2 = {1, 2, 3, 6}

print('\nSkup 1:')
print('\n', skup1)

print('\nSkup 2:')
print('\n', skup2)

print('\nPresjek s metodom "intersection()":')
print('\n', skup1.intersection(skup2))

print('\nPresjek s operatorom "&":')
print('\n', skup1 & skup2)

# SKUPOVNA RAZLIKA metoda "difference()" ili operator "-"

skup1= {1, 5, 1, 5, 4, 7, 8, 2, 3, 2} 
skup2 = {1, 2, 3, 6}

print('\nSkup 1:')
print('\n', skup1)

print('\nSkup 2:')
print('\n', skup2)

print('\nSkupovna razlika s metodom "difference()":')
print('\n', skup1.difference(skup2))
print('\n', skup2.difference(skup1))

print('\nSkupovna razlika s operatorom "-":')
print('\n', skup1 - skup2)
print('\n', skup2 - skup1)

# KOMPLEMENT PRESJEKA metoda "symetric_difference()" ili operator "^"

skup1= {1, 5, 1, 5, 4, 7, 8, 2, 3, 2} 
skup2 = {1, 2, 3, 6}

print('\nSkup 1:')
print('\n', skup1)

print('\nSkup 2:')
print('\n', skup2)

print('\nKomplement presjeka s metodom "symetric_difference()":')
print('\n', skup1.symmetric_difference(skup2))
print('\n', skup2.symmetric_difference(skup1))


print('\nKomplement presjeka s operatorom "^":')
print('\n', skup1 ^ skup2)
print('\n', skup2 ^ skup1)

skup1 = set('RUMPELŠTILSKIJ')
skup2 = set('ČIRIBUĆIRIBA')

print('\nSkup 1: RUMPELŠTILSKIJ')
print('\nSkup 2: ČIRIBUĆIRIBA')

print('\nSkupovi', skup1, skup2, sep='\n')

print('\nUnija: ', skup1 | skup2)

print('\nPresjek: ', skup1 & skup2)

print('\nSkupovna razlika 1-2: ', skup1 - skup2)
print('\nSkupovna razlika 2-1: ', skup2 - skup1)

print('\nKomplement presjeka: 1^2', skup1 ^ skup2)
print('\nKomplement presjeka: 2^1', skup2 ^ skup1)
input()



