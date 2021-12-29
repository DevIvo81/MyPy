upit = 'UPIT'

ime = input(f'{upit}: Upisite Vase ime: ')
prezime = 'Peric'
godina_rodenja = 1995

# poruka = f'Godine {godina_rodenja}. je rodena osoba: {ime} {prezime}.'
# print(poruka)

print(f'Godine {godina_rodenja}. je rodena osoba: {ime} {prezime}.')

print(f'Ime:\t\t{ime}')
print(f'Prezime:\t{prezime}')

red_hex = 'EA'
red_dec = int(red_hex, 16)

print()
print(f'Heksadekadski zapis:\t{red_hex}')
print(f'Dekadski zapis:\t\t{red_dec}')
print()
print(f'Dekaski zapis heksadekadskog broja "{red_hex}" je {red_dec}.')