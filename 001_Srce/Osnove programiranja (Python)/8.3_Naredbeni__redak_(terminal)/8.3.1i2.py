'''Kreirajte zadatak koji će se samostalno izvršavati svaku minutu. 
Skripta koju će kreirani zadatak izvršiti neka ispiše prilikom svakog 
izvršavanja u neku proizvoljnu datoteku vrijednost "x". Obratite 
pozornost da se sadržaj datoteke ne smije brisati, već se mora 
prilikom svakog izvršavanja u datoteku dopisati jedan "x".'''

import os, sys
os.system('cls')

with open('Srce\\8.3\\Fajlic.txt', 'a') as f:
    f.write('X' + ' ')
input()
