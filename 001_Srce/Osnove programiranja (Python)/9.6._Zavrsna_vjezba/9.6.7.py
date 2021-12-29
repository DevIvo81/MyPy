'''7.  * S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz 
znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog 
niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u 
ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza, 
prvo sljedeće veliko slovo u nastavku ulaznog niza itd. Novokreirani 
niz ispišite na zaslon. U nastavku se nalazi primjer:
Ulazni niz: ifeFemFEkej83FkW 
Izlazni niz: FeFkFkW'''
import os
os.system('cls')

ulazniNiz = 'ifeFemFEkej83FkW'
# izlazniNiz: 'FeFkFkW'
izlazniNiz = ''

veliko_slovo = True

for e in ulazniNiz:
    if 'A'<= e <='Z'and veliko_slovo == True:
        izlazniNiz += e
        veliko_slovo = False
    elif 'a'<= e <='z'and veliko_slovo == False:
        izlazniNiz += e
        veliko_slovo = True

print(ulazniNiz)
print(izlazniNiz)
    