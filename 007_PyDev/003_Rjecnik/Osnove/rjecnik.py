prazan_rjecnik = {}

osobe = {
    '1234': 'Petar Peric',
    '4321': 'Ana Anic',
    '6789': 'Marko Maric',
    '9876': 'Iva Ivic'
}

osoba = osobe['1234']
# print(osoba)

nova_osoba = 'Marija Maric'
osobe['2584'] = nova_osoba

#print(osobe)

jos_jedna_osoba = 'Josip Josipovic'
osobe['3589'] = jos_jedna_osoba
#print(osobe)


# kljuc = input("unesite svoj OIB")
# vrijednost = input("unesite puno ime i prezime")
# osobe[kljuc] = vrijednost

# print(osobe)

print(osobe.keys())
print(osobe.values())
print(osobe.items())
print('\n')

for key in osobe.keys():
    #print(key, end=' ')
    print(osobe[key])
print('\n')

for value in osobe.values():
    print(value)
print('\n')


for kljuc, vrijednost in osobe.items():
    osobe[kljuc] = ''
    #print(f'Key: {kljuc}\tValue: {vrijednost}')


for kljuc, vrijednost in osobe.items():
    print(f'Key: {kljuc}\tValue: {vrijednost}')




# Internet domene TLD - top level domain
# Kupci - sifra_kupca : naziv
# Proizvodi - sifra proizvoda : naziv proizcoda

# VRIJEDNOST -> listu
# kljuc : lista