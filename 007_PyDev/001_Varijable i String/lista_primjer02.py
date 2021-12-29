# brojevi = []
# print(brojevi)

# broj_brojeva = int(input('Koliko brojeva zelite unijeti? '))

# # prvi_broj = int(input('Upisite prvi broj: '))
# # brojevi.append(prvi_broj)

# # drugi_broj = int(input('Upisite drugi broj: '))
# # brojevi.append(drugi_broj)

# # treci_broj = int(input('Upisite trevi broj: '))
# # brojevi.append(treci_broj)

# for broj_ponavaljanja in range(broj_brojeva):
#     broj = int(input(f'Upisite {broj_ponavaljanja + 1}. broj: '))
#     brojevi.append(broj)


# print(brojevi)


# range(pocetak, kraj, korak) VAZNO KRAJ NIJE UKLJUCEN

# range(5) -> pocetak=0, kraj=5, korak=1
# range(1, 101) -> pocetak=1, kraj=101, korak=1
# range(1, 101, 4) -> pocetak=1, kraj=101, korak=4

brojevi = []
print()
broj_elemenata = len(brojevi)
print('Broj elemenata liste', broj_elemenata)
print()

for broj in range(100):
    brojevi.append(broj + 1)

print()
for element in brojevi:
    print(element, end=' ')

print()
broj_elemenata = len(brojevi)
print('Broj elemenata liste', broj_elemenata)
print()


print(f'Indeks : Vrijednost')
for indeks in range(len(brojevi)): # range(100)
    print(f'{indeks} :\t {brojevi[indeks]}')


