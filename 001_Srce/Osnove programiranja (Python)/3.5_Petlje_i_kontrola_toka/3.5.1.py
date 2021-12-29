'''U varijablu r spremite neki broj koji predstavlja radijus kugle. Ako je 
radijus ispravno upisan (radijus ne može biti negativan), ispišite 
radijus i volumen kugle, 𝑉 = 4/3 × 𝑟3 × 𝜋. Inače, ispišite poruku da je 
vrijednost u varijabli "r" neispravna.'''
import os
os.system('cls')

pi = 3.1415

while True:
    r = int(input("\nUnesi radijus kugle kojoj želiš izračunati volumen: "))
    if r <=0:
        print("\nRadijus ne može biti negativan ili jednak nuli!")
    else:
        v = 4/3 * r**3 * pi
        print("\nVolumen kugle radijusa ", r, " iznosi V = ", round(v))
        
    if input("\nŽelite li pokušati opet? [DA/NE] ").upper() == 'NE':    
        break



