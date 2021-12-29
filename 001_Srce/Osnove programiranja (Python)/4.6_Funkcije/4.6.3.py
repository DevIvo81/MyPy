'''3.  Napišite funkciju mnozenje() koja može primiti 2 vrijednosti, od 
kojih je druga vrijednost unaprijed zadana, sami odredite broj koji 
ćete pridružiti unaprijed zadanoj vrijednosti. Funkcija mora izračunati 
i ispisati rezultat množenja. U glavnom dijelu programa pozovite funkciju 
dva puta. Kod prvog poziva funkcije, kao argumente funkcije navedite 
dvije vrijednosti (vrijednost drugog argumenta neka bude drugačija od 
unaprijed zadane vrijednosti). Drugi put funkciju pozovite samo jednim 
argumentom.'''

import os
os.system('cls')

def množenje(a, b=10):
    print("\nUmnožak je ", a*b)

množenje(15, 20)
print()
množenje(15)
