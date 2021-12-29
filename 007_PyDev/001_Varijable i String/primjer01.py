# Puno ime i prezime je Petar Peric

ime = input('Molimo upisite Vase ime: ')
prezime = input('Molimo upisite Vase prezime: ')

# puno_ime = ime + ' ' + prezime
puno_ime = '{} {}'.format(ime, prezime)

poruka = 'Puno "ime i prezime" je: {} {}.'.format(ime, prezime)

poruka_krace = f"Puno ime i prezime je: \"{prezime} {ime}\"."

print()
print(poruka)
print()
print(poruka_krace)
print()