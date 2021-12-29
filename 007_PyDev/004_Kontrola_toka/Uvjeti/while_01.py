from typing import no_type_check


uvjet = False
while uvjet:
    print('Pozdrav iz WHILE petlje')

print('Pozdrav IZVAN WHILE petlje')


# brojevi = []
# for broj in range(1, 10 + 1):
#     brojevi.append(broj)

# KRACI NACIN
brojevi = [ broj for broj in range(1, 10 + 1) ]

for br in brojevi:
    print(br, end=' ')
print()

brojac = 100
while brojac > len(brojevi):
    # print(brojevi[brojac], end=' ')
    print('Pozdrav iz WHILE')
    brojac += 1