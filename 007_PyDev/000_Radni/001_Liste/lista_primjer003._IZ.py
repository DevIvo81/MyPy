import os
os.system('cls')

# recenica = 'Python Developer program obrazovanja'

# print()

# for slovo in recenica:
#     print(slovo, end=' ')

# print()

# print(f'\nIndeks: Slovo\n')
# for i in range(len(recenica)):
#     print(f'{i} :\t {recenica[i]}')

# print()

# broj_slova = len(recenica)
# print(broj_slova)
# print()

#       012345
boja = 'EA4526'

# SLICE NOTATION

# range(pocetak, kraj, korak)
# naziv_liste[pocetak:kraj:korak]

prva_dva_elementa = boja[ 0 : 2 : 1 ]

print()
print(prva_dva_elementa)
print()

druga_dva_elementa = boja [ 2 : 4 : 1]
print()
print(druga_dva_elementa)
print()

zadnja_dva_elementa = boja [ 2:4:-2 ]
print()
print(zadnja_dva_elementa)
print()
