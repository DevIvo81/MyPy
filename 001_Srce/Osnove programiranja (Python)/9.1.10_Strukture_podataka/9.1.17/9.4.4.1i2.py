'''1. Napravite n-terac u kojem su pohranjeni samoglasnici. Ispišite 
prva tri samoglasnika.
2. Isprobajte promijeniti ili izbrisati element n-terca.'''
import os
os.system('cls')

vocals = ('A', 'E', 'I', 'O', 'U')

print(vocals[:3])

# vocals[0] = 'E'

# del vocals[0]

del vocals

print(vocals)