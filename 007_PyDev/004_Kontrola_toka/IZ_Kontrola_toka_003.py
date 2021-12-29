import os
os.system('cls')

'''
# PROVJERA DJELJIVOSTI

lista = [i for i in range(1, 31)]
print(lista)
for broj in lista:
    if broj % 9 == 0:
        print(f'\nBroj {broj} je djeljiv s 9')
    if broj % 6 == 0:
        print(f'\nBroj {broj} je djeljiv s 6')
    if broj % 3 == 0:
        print(f'\nBroj {broj} je djeljiv s 3')
print()
print('_'*len(lista))
'''

    
# PROVJERA PALINDROMA

print('\nPROVJERA PALINDROMA')
print('_'*19)
while True:
    
    rijec = input('\nUpiši riječ ili rečenicu - ')
    low_rijec = rijec.lower().replace(' ', '')

    if low_rijec == low_rijec[ : : -1]:
        print(f'\nUpisana riječ odnosno rečenica JE palindrom!')
    else:
        print(f'\nUpisana riječ odnosno rečenica NIJE palindrom!')

    if input('\nJoš jednom [Y / N] ? ').lower() == 'n':
        break



    
        




