# import Blok
import os
os.system('cls')

# Blok deklaracije klasa, funkcija, varijabli...

def pozdrav(ime):
    """
    Funkcija koja na konzolu ispisuje
    pozdravnu poruku uz argument 'ime' koje smo
    joj proslijedili.
    Ako je prijepodne ispisuje Dobro jutro
    Ako je poslijepodne ispisuje Dobar dan
    Ako je poslije 19 sati ispisuje Dobra večer
    """
    from datetime import datetime as dt
    
    if dt.now().hour < 10:
        print(f'\nDobro jutro, {ime}. Kako ste danas?')
    elif 10 < dt.now().hour < 19:
        print(f'\nDobar dan, {ime}. Kako ste danas?')
    else:
        print(f'\nDobra večer, {ime}. Kako ste?')
    
    
# MAIN blok
korIme = input('\nUpiši ime: ')
pozdrav(korIme)
pozdrav('Pero Peric')
pozdrav('Ana Anic')

    