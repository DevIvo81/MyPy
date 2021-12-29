'''5.  S tipkovnice učitajte broj proizvoljne vrijednosti. Pomoću 
ternarnog operatora detektirajte je li učitani broj paran ili neparan. 
Ako je učitani broj paran, ispišite na ekran: "Paran!", ako pak je 
neparan, ispišite na ekran: "Neparan!".'''
import os
os.system('cls')
broj = int(input('\nUpiši broj: '))

print(f'\nBroj {broj} je paran') if broj % 2 == 0 else print(f'\nBroj {broj} je neparan')


