znak = input('\nUpiši znak: ')
pon = int(input('\nUpiši broj ponavljanja: '))

lista = []
for i in range(pon):
    lista.append(znak)

print('\nIspis ', end='')
print(*lista, sep='-')
print()
input()