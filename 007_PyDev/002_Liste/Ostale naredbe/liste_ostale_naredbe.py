# brojevi = []
# for broj in range(21):
#     brojevi.append(broj)


# print('POCETNI ISPIS')
# for broj in brojevi:
#     print(broj, end=' ')

# print()

# del brojevi[5]

# print()
# for broj in brojevi:
#     print(broj, end=' ')


# brojevi[5] = 5

# print()
# for broj in brojevi:
#     print(broj, end=' ')


# brojevi.insert(5, 5)

# print()
# for broj in brojevi:
#     print(broj, end=' ')
# print()


# brojevi.clear()
# print('\nPRINT nakon clear()')
# for broj in brojevi:
#     print(broj, end=' ')
# print()


# brojevi_kopija = brojevi.copy()
# print('\nPRINT nakon copy()')
# for broj in brojevi_kopija:
#     print(broj, end=' ')
# print()


# lista= [1,2,3]
# lista_kopija = lista.copy()
# lista.clear()
# print(lista_kopija) # dati 1,2,3

# print('\n\n')
# print('Duzina liste', len(brojevi))
# brojevi.insert(10, 15)
# print('Duzina liste', len(brojevi))
# broj_ponavaljanja = brojevi.count(15)
# print('Broj ponavljanja', broj_ponavaljanja)


# print('\n\n')
# indeks_elementa = brojevi.index(50)
# print('Indeks elementa 15:', indeks_elementa)

# print(brojevi[indeks_elementa])

# print(brojevi[10])
# print(brojevi[16])

# #help(list.index)
# ''' index(self, value, start=0, stop=9223372036854775807, /)      
#     Return first index of value
# '''

# print()
# rijeci = ['Algebra', 'Python', 'Programiranje']
# print()

# for rijec in rijeci:
#     brojevi.extend(znak.upper() for znak in rijec)

# print(brojevi)

# print()
# print(*brojevi) # end je UVIJEK = ' '
# print()
# print(*brojevi, sep='\n')


# print()
# print('REVERSED')
# for broj in reversed(brojevi):
#     print(broj, end=' ')


# print('\n', brojevi)

# brojevi.reverse()
# print('REVERSE')
# print(brojevi)

# print('POCETNI ISPIS')
# for broj in brojevi:
#     print(broj, end=' ')

# print()

# rijeci = ['Algebra', 'Python', 'Programiranje']

# for broj in brojevi[ : : -1]:
#     print(broj, end=' ')


# kopija_liste = brojevi[ : : -1]
# kopija_liste.reverse()

# print('brojevi', brojevi)
# print('kopija_liste',kopija_liste)

rijeci = ['Osijek', 'Algebra', 'Python', 'Programiranje']
#print(rijeci)
for rijec in rijeci:
    print(rijec)


rijeci.sort(reverse=True)
#print(rijeci)
print()
for rijec in rijeci:
    print(rijec)

# help(list.sort)

