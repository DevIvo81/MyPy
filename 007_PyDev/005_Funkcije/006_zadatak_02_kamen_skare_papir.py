import os
from random import randint as rnd
from random import shuffle as shf
os.system('cls')

izbornik = '''
    Izbornik opcija(upišite opciju koju želite):
    1. kamen
    2. skare
    3. papir    
'''

opcije = ['kamen', 'skare', 'papir']
print(opcije)
# nove_opcije = shf(opcije)
# izbor_racunala = opcije[0]
# print(izbor_racunala)

# izbor_racunala = opcije[rnd(0, 2)]
# print(izbor_racunala)

# print(izbornik)


def izbornik():
    print(
'''
    Izbornik opcija(upišite opciju koju želite):
    1. kamen
    2. skare
    3. papir    
''')

def provjeri_rezultat(izbor_igraca_1, izbor_igraca_2):

    if izbor_igraca_1 == izbor_igraca_2:
        print('\nNeriješeno')
    elif izbor_igraca_1 == 1 and izbor_igraca_2 == 2:
        print('Računalo je pobijedilo!')
    else:
        print('Pogrešan unos!')

while True:
    
    izbor_racunala = rnd(1,3)
    print(izbor_racunala)

    izbornik()
    
    izbor_korisnika = int(input('\nUpišite svoj izbor: '))
    