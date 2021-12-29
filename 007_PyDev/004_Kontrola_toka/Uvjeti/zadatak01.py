'''
Napisite program koji ce traziti od korisnika unos znaka
i broj ponavljanja znaka te za unesene vrijednosti M 5
ispisati na ovakav nacin:
M-M-M-M-M

Iza zadnjeg znaka NE smije biti znak minus
NE OVAKO 
M-M-M-M-M-
'''

# znak = input('Upisite znak: ')
# broj_ponavljanja = int(input('Upisite broj ponavljanja: ')) # 5

# for i in range(broj_ponavljanja): # range(5) -> 0, 1, 2, 3, 4 
#     if i == (broj_ponavljanja - 1):
#         print(f'{znak}')
#     else:
#         print(f'{znak}', end='-')



znak = input('\nUpiši znak: ')
pon = int(input('\nUpiši broj ponavljanja: '))

lista = []
for i in range(pon):
    lista.append(znak)

print('\nIspis ', end='')
print(*lista, sep='-')
print()
input()

'''
value, value, value, value

value-value-value-value
'''