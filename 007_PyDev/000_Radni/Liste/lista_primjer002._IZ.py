# brojevi = []

# prvi_broj = int(input('Upišite prvi broj: '))
# brojevi.append(prvi_broj)

# drugi_broj = int(input('Upišite drugi broj: '))
# brojevi.append(drugi_broj)

# treci_broj = int(input('Upišite drugi broj: '))
# brojevi.append(treci_broj)

# for broj_ponavljanja in range(5):
#     broj = int(input(f'Upisite {broj_ponavljanja +1}. broj: '))
#     brojevi.append(broj)

# print(brojevi)

brojevi = []

for broj in range(1, 101):
    brojevi.append(broj)
print(brojevi)

print(f'\nIndeks: Vrijednost\n')
for i in range(len(brojevi)):
    print(f'{i} :\t {brojevi[i]}')
