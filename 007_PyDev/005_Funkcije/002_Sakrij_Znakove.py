# ZADATAK: Kupovina u online dućanima je postala svakodnevica
#     Za to koristimo našu kreditnu karticu
#     Napišite program koji će uneseni broj kartice od korisnika
#     zaštititi tako da sve znakove osim zadnja četiri maskira pomoću # znakova
#     Primjer: Broj 3698521478523691234

def sakrij_znakove(tekst):
    zasticeni_tekst = ''
    if len(tekst) <= 5:
        return f'\nERROR! Prekratko!'
    else:
        limit_zastite = len(tekst) - 4
        indeks = 0
        for znak in tekst:
            if indeks < limit_zastite:
                zasticeni_tekst += '#'
                indeks += 1
            else:
                zasticeni_tekst += znak
                indeks += 1
    return zasticeni_tekst

kartica = input('\nUpišite broj Vaše kartice: ')

print(f'\nNezaštićeni prikaz vaše kartice je:\n\n{kartica}')
print(f'\nZaštićeni prikaz vaše kartice je:\n\n{sakrij_znakove(kartica)}')