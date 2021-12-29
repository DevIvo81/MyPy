import os
os.system('cls')

python_lista = ['jedan', 'dva', 'tri', 'četiri', 
'pet', 'šest', 'sedam', 'osam', 'devet', 'deset']
prazna_lista = []

# 5 element liste -> 5-1 zato jer lista počinje s 0
# python_lista[4]

# print(f'Prvi el. liste je {python_lista[0]}')

# print(prazna_lista[0])

# prazna_lista[1] = 3

# prazna_lista.append(2)

# help(range)
# range(start, stop, step) 

broj_elemenata = len(python_lista)

for indeks in range(5):   
    print(python_lista[indeks])
print()

for element in python_lista:
    print(element)

pola_liste = broj_elemenata // 2

for i in range(pola_liste):
    print(python_lista[i])

