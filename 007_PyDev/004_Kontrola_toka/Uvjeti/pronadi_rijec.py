'''
ZADATAK: U generičkom tekstu 'Lorem ipsum ...' (https://www.lipsum.com/) 
        pronađite koliko se pojavljuje neka riječ.
'''


tekst = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quisque posuere porttitor ex, et aliquet arcu ullamcorper sit amet. \
    Fusce arcu diam, cursus ut venenatis et, condimentum et nunc. '
    'Ut at sapien eu mauris placerat vehicula. '
    'Vestibulum neque neque, feugiat id metus nec, gravida mattis risus. '
    'Morbi ac nunc sagittis, ultrices urna vitae, feugiat orci. '
    'Cras id dui orci. Fusce facilisis varius nulla vel scelerisque.'
    'Etiam lectus libero, tempus sit amet posuere at, ornare at leo. '
    'Nunc dui enim, pharetra sed ligula eget, rhoncus tincidunt neque. '
    'Sed enim metus, gravida a elementum eu, convallis eget urna. '
    'Vivamus condimentum lectus vehicula, aliquet leo eu, congue eros. '
    'Phasellus rutrum, arcu in auctor vulputate, lorem magna lobortis elit, '
    'non dignissim massa tellus vel purus. '
    'Integer feugiat ultrices euismod. Ut viverra porttitor mauris, '
    'vitae euismod nisl semper ut. '
    'Nullam eu odio pulvinar, iaculis orci ac, porttitor erat. '
    'Aenean vel dolor in purus ullamcorper bibendum at ut turpis.'
    ' '
    'Suspendisse dapibus odio sed urna hendrerit lacinia. '
    'Quisque varius purus dolor, tincidunt dapibus lacus imperdiet et. '
    'Nunc sapien mi, faucibus in ullamcorper eget, auctor vel mauris. '
    'Pellentesque tempor eget risus a vulputate. '
    'Nullam condimentum, ipsum ut placerat consectetur, '
    'purus orci volutpat est, id feugiat sem sem id ipsum. lorem '
    'Nam auctor tempor enim, sit amet laoreet nibh cursus in. '
    'Fusce elementum dolor ac felis condimentum, a tincidunt quam facilisis.')

print(tekst)

# help(str.split)
# help(str.replace)
lista_rijeci = tekst.lower().replace('.', '').replace(',', '').split(' ')
# print(*lista_rijeci, sep='\n')

trazena_rijec = 'Lorem' # input()
brojac = 0

for rijec in lista_rijeci:
    if rijec.lower() == trazena_rijec.lower():
        brojac += 1
    # else:
    #     pass

print(f'Rijec {trazena_rijec} se u tekstu ponavlja {brojac} puta.\n')


# Kratki oblik
lista_rijeci = tekst.lower().replace('.', '').replace(',', '').split(' ')
count_rijeci = lista_rijeci.count(trazena_rijec.lower())
print(f'Rijec {trazena_rijec} se u tekstu ponavlja {count_rijeci} puta.\n')