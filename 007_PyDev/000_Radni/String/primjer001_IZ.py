import os
os.system('cls')

ime = input('Molimo upišite ime: ')
prezime = input('Molimo upišite prezime: ')

puno_ime = '{} {}'.format(ime, prezime)

poruka = 'Puno ime i prezime je : {} {}'.format(ime, prezime)

poruka_krace = f'Puno ime i prezime je : {prezime} {ime}.'

poruka_krace = f"Puno ime i prezime je : \"{prezime} {ime}\"."

print(poruka)
print()
print(poruka_krace)
print()

