
'''11. ** Napišite generatorsku funkciju imena bottles(brojBoca, 
nazivNapitka). Ova funkcija mora vratiti generator koji 
otpušta stihove pjesme: "99 Bottles of Beer". Svaki stih ove 
pjesme ima za jedan napitak manje od prethodnog stiha, tako 
dugo dok se ne istroše svi napitci. Predefinirana vrijednost za 
broj boca je 99, dok je predefinirana vrijednost za naziv napitka 
"beer". U nastavku slijedi primjer ispisa za dani parametar 
brojBoca = 4.
4 bottles of beer on the wall, 4 bottles of beer.
Take one down and pass it around, 3 bottles of beer on the wall. 
3 bottles of beer on the wall, 3 bottles of beer.
Take one down and pass it around, 2 bottles of beer on the wall. 
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall. 
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on 
the wall.
No more bottles of beer on the wall, no more bottles of beer. 
Go to the store and buy some more, 99 bottles of beer on the 
wall.'''
import os
os.system('cls')

brojBoca = input('\nUpiši broj boca: ')
brojBoca = int(brojBoca)

nazivNapitka = 'beer'

def bottles(brojBoca, nazivNapitka):
    yield print(f'{brojBoca} bottles of {nazivNapitka} on the wall, {brojBoca} bottles of beer.\nTake one down and pass it around, {brojBoca-1} bottles of {nazivNapitka} on the wall.')
    
gen = bottles(brojBoca, nazivNapitka)

for i in range(brojBoca):
    print(next(gen))

    
    





