
import os
os.system('cls')

def jePalindrom(rijec):
    obrnutaRijec = rijec[ : : -1]
    if obrnutaRijec.lower() == rijec.lower():
        return True
    else:
        return False


def ispis(poruka):
    print(poruka, end='\n\n')



rijec = 'Kapak'

if jePalindrom(rijec):
    ispis(f'Riječ {rijec} JE palindrom!')
else:
    ispis(f'Riječ {rijec} NIJE palindrom!')

ispis(rijec)