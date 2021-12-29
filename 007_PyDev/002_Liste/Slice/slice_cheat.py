import os
os.system('cls')

brojevi = []
for i in range(101):
    brojevi.append(i)

# print('\n',brojevi)

# Primjer 01
# od 20 do 46, svaki 6-i

print('naziv_liste[POČETAK : KRAJ : KORAK]')
print('naziv_liste[20 : 46 : 6]')
primjer_01 = brojevi[20 : (46+1) : 6]
for i in primjer_01:
    print(i, end=' ')
print()
print()

# Primjer 02
# od 20 do 46 (NIJE UKLJ.), KORAK = 1 (DEFAULT)
print('naziv_liste[POČETAK : KRAJ] -> KORAK=1')
print('naziv_liste[20 : 46]')
primjer_02 = brojevi[20 : 46]
for i in primjer_02:
    print(i, end=' ')
print()
print()

# Primjer 03
# od 20 do KRAJA (JE UKLJ.), KORAK = 1 (DEFAULT)
print('naziv_liste[POČETAK : KRAJ] -> KORAK=1')
print('naziv_liste[20 : ]')
primjer_03 = brojevi[20 : ]
for i in primjer_03:
    print(i, end=' ')
print()
print()

# Primjer 04
# od POČETAK do 46 (NIJE UKLJ.), KORAK = 1 (DEFAULT)
print('naziv_liste[ : 46] -> KORAK=1')
print('naziv_liste[ : 46]')
primjer_04 = brojevi[ : 46]
for i in primjer_04:
    print(i, end=' ')
print()
print()


# Primjer 05
# od POČETAK do KRAJ (JE UKLJ.), KORAK = 1 (DEFAULT)
# CIJELA LISTA
print('naziv_liste[ : ] -> KORAK=1')
print('naziv_liste[ : ]')
primjer_05 = brojevi[ : ]
for i in primjer_05:
    print(i, end=' ')
print()
print()


# Primjer 06
# od NEG POČETAK do KRAJ (JE UKLJ.), KORAK = 1 
print('naziv_liste[-START : ] -> KORAK=1')
print('naziv_liste[-2 : ]')
primjer_06 = brojevi[-2 : ]
for i in primjer_06:
    print(i, end=' ')
print()
print()


# Primjer 07
# od POČETAK do NEG-KRAJ (NIJE UKLJ.), KORAK = 1 
print('naziv_liste[ : -KRAJ] -> KORAK=1')
print('naziv_liste[ : -2]')
primjer_07 = brojevi[ : -2]
for i in primjer_07:
    print(i, end=' ')
print()
print()


# Primjer 08
# od POČETAK do NEG-KRAJ (JE UKLJ.), KORAK = -1 
print('naziv_liste[ : : -KORAK] -> KORAK= -1')
print('naziv_liste[: : -1]')
primjer_08 = brojevi[: : -1]
for i in primjer_08:
    print(i, end=' ')
print()
print()


# Primjer 09
# od POČETAK do KRAJ (JE UKLJ.), KORAK = -1 
print('naziv_liste[POČETAK : : -KORAK] -> KORAK= -1')
print('naziv_liste[2: : -1]')
primjer_09 = brojevi[2 : : -1]
for i in primjer_09:
    print(i, end=' ')
print()
print()


# Primjer 10
# od POČETAK do -KRAJ (NIJE UKLJ.), KORAK = -1 
print('naziv_liste[: -KRAJ : -KORAK] -> KORAK= -1')
print('naziv_liste[: -3 : -1]')
primjer_10 = brojevi[: -3 : -1]
for i in primjer_10:
    print(i, end=' ')
print()
print()


# Primjer 11
# od -POČETAK do KRAJ (JE UKLJ.), KORAK = -1 
print('naziv_liste[-POČETAK: KRAJ : -KORAK] -> KORAK= -1')
print('naziv_liste[-3: : -1]')
primjer_11 = brojevi[-3 : : -1]
for i in primjer_11:
    print(i, end=' ')
print()
print()