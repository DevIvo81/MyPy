'''
A       B       A and B     A or B
True    True    True        True
True    False   False       True
False   True    False       True
False   False   False       False
'''

# prvi_uvjet = True
# drugi_uvjet = False
# treci_uvjet = True

# if prvi_uvjet:
#     print('Prvi Uvjet je TRUE')

# if drugi_uvjet:
#     print('ELIF Drugi Uvjet je TRUE')

# else:
#     print('Pozdrav iz ELSE')


'''
Kreirajte listu od 1 do broja 30. 
Ispišite sve brojeve koji su djeljivi s 3, 6 i 9
Provjera je li broj djeljiv s nekim drugim 
radimo pomoću % (modulo) operanda.
15 % 3 NEMA ostatka, odnosno to je 0 pa je 15 djeljiv s 3.
16 % 3 je 1, odnosno NIJE jednak 0 pa 16 NIJE djeljiv s 3.
'''

brojevi = []

for broj in range(1, 31):
    brojevi.append(broj)

print('Pomocu IF - IF')
for broj in brojevi:
    if broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 3')
    if broj % 6 == 0:
        print(f'Broj {broj} je djeljiv s 6')
    if broj % 9 == 0:
        print(f'Broj {broj} je djeljiv s 9')
    else:
        print(f'Broj {broj} NIJE djeljiv s 3, 6 ili 9')
print()

print('Pomocu AND - OR')
for broj in brojevi:
    if broj % 9 == 0 or broj % 6 == 0 or broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 9, 6 ili 3')
    else:
        print(f'Broj {broj} NIJE djeljiv s 3, 6 ili 9')
print()