# ZADATAK: Napišite program koji provjerava je li unesena riječ palindrom.
# Palindrom je riječ koja se jednako piše (i čita) s lieva na desno i s desna na lijevo

rijec = input('Upisite rijec za koju zelite provjeriti je li PALINDROM:\n')
#print(rijec)

obrnuta_rijec = rijec[ : : -1]
#print(obrnuta_rijec)

if rijec.upper() == obrnuta_rijec.upper():
    print(f'Rijec {rijec} JE palindrom.')
else:
    print(f'Rijec {rijec} NIJE palindrom.')


print()
print('Kraci nacin pisanja')
if rijec.lower() == rijec[ : : -1].lower():
    print(f'Rijec {rijec} JE palindrom.')
else:
    print(f'Rijec {rijec} NIJE palindrom.')