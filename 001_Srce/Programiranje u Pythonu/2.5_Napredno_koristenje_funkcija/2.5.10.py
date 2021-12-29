'''10. ** Pronađite na Internetu u službenoj Python 3 dokumentaciji 
funkcionalnost i način korištenja ugrađene funkcije map(). 
Službenu Python 3 dokumentaciju možete pronaći na URL-u: 
https://docs.python.org/3/.

Kreirajte listu od 5 proizvoljnih vrijednosti koje će predstavljati 
temperaturu izraženu u stupnjevima Celzijevim. Napišite 
bezimenu funkciju koja će uz pomoć funkcije map()generirati 
vrijednost temperature izražene u Farenhajtima. 
Formula: ( 𝑥 × 9 / 5) + 32 , "x" je vrijednost izražena u stupnjevima 
Celzijevim. Tako dobivenu listu ispišite na ekran.'''
import os
os.system('cls')

def konverzija(celzij):
    return celzij*9/5 + 32

celziji = [0, 180, 200, 220, 240]

fahrici = map(konverzija, celziji)

print(list(fahrici))