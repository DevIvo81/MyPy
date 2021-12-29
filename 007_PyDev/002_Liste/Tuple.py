# osobe = {
#     '1234' : 'Petar Perić',
#     '1234' : 'Ana Anić',
#     '1234' : 'Marko Marić',
#     '1234' : 'Iva Ivić'
# }

# print(osobe.keys())
# print(osobe.values())
# print(osobe.items())

n_terac = ('Python', 'Algebra', 'Programiranje', 'Python')
print(f'\nTUPLE {n_terac}')

# prvi_element = n_terac[0]
# print(f'\n1. element {prvi_element}')

# drugi_element = n_terac[1]
# print(f'\n2. element {drugi_element}')

# n_terac[0] = 'Prvi element'
# del n_terac[0]
# n_terac.append('Pero Perić')

# help(tuple)

# broj_ponavljanja = n_terac.count('Python')
# print(f'\nPython se u tupleu pojavljuje {broj_ponavljanja}')

# indeks_elementa = n_terac.index('Python', 1)
# print(f'\nINDEKS je {indeks_elementa}')

# for element in n_terac:
#     print('\n', element.upper())

# lista = list(n_terac)
# print(f'\nTUPLE {n_terac}')
# print(f'\nLista {lista}')

# lista[3] = 'C++'
# print(f'\nLista {lista}')

# my_tuple = tuple(lista)
# print(f'\nMY TUPLE nakon izmjena u listi : ')


# osobe = {
#     '1234' : 'Petar Perić',
#     '4321' : 'Ana Anić',
#     '5678' : 'Marko Marić',
#     '8765' : 'Iva Ivić'
# }

# print(f'Rjecnik Osobe {osobe}')
# tuple_from_dictionary = tuple(osobe.items())
# # dobivamo ključeve
# print(f'\nTUPLE OD ITEMS() {tuple_from_dictionary}')
# # tuple_from_dictionary = tuple(osobe.values())
# # # dobivamo vrijednosti rječnika
# # print(f'\nTUPLE OD OSOBE {tuple_from_dictionary}')
# # tuple_from_dictionary = tuple(osobe.items())
# # # dobivamo vrijednosti rječnika
# # print(f'\nTUPLE OD OSOBE {tuple_from_dictionary}')

# print(n_terac[ : : -1])

my_tuple = 'Python', 'Algebra', 'Programiranje', 'Python', 3, 514)
print(type(my_tuple))

lista = []
dictio = {}
