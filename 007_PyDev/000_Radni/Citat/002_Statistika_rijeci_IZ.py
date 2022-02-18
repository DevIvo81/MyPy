'''
Na internetu nađite nekakav tekst (citat, ulomak iz knjige …) i izradite statistiku riječi tako da:

Navedete koliko riječi ima
    - Koliko slova ima najduža riječ te koja je to riječ
    - Koliko slova ima najkraća riječ te koja je to riječ
    - Koliko riječi ima koje imaju 1 slovo, koliko koje imaju 2 slova itd.
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')
    


# citatSaNeta = f'''
# Želite li izgraditi web-aplikaciju, posegnite za Python programskim jezikom. 
# Morate li automatizirati neki zadatak na IT sustavu, rješenje pronađite u 
# Pythonu. Kada želite pronaći najčešće boje na slici, Python nudi rješenje.
# Također je široko prihvaćen u ključnim područjima poput analitike podataka, 
# strojnog učenja, internetske sigurnosti i robotike. Osim toga, Python je postao 
# biblijski jezik izbora za mnoge velike multinacionalne organizacije, uključujući 
# Google, Facebook, Apple i Citibank.
# '''


# pretvaranje citata u listu riječi

def obradaTeksta(tekst):

    listaRijeci = tekst.split()

    brojRijeci = len(listaRijeci)
    print(f'\nTekst sadrži {brojRijeci} riječi')

    duljineRijeci = [len(rijec) for rijec in listaRijeci]

    duljineRijeci.sort()

    maxDuljinaRijeci = duljineRijeci[-1]
    print(f'\nNajduže riječi imaju {maxDuljinaRijeci} slova')
    print(f'\nRiječi poredane po duljini:')

    def prebrojavanje():
        
        # Eliminiranje duplikata   
        bezPonavljanjaDuljina = list(set(duljineRijeci))

        for brojSlova in bezPonavljanjaDuljina:
            print(f'\n{brojSlova} slova -- ', end=' ')
            for rijec in listaRijeci:
                if len(rijec) == brojSlova:
                    print(f' "{rijec}" ', end='')
            print()
        print()
        
        
    prebrojavanje()
    
while True:
    
    obradaTeksta(input('Upišite ili zalijepite tekst\n\n --> '))
    
    if input('\nNovi unos (0 za prekid)? --> ') == '0':
        print('\nDo sljedećeg puta, pozdrav!\n')
        break