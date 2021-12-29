'''* Napišite program koji će u varijablu spremiti neku vrijednost 
temperature (izražene u stupnjevima Celzijevim). Na ekran ispisati 
vrijednost temperature u farenhajtima.Formula: ( 𝑥 × 9/5 ) + 32 , x 
je vrijednost izražena u stupnjevima Celzijevim.'''

import os
os.system('cls')

c = int(input("\nUnesi temperaturu u °C: "))

f = round((c*9/5)+32)

print("\n", c, " °C je ", f, " °F")
