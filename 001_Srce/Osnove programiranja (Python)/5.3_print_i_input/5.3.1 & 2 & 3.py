'''Napišite program koji se sastoji od pet varijabli. S jednim pozivom 
funkcije print()ispišite svih pet vrijednosti.'''

''''Nastavno na prethodni zadatak, doradite poziv funkcije print() 
tako da vrijednost svake pojedine varijable bude u novom redu.'''
import os
os.system('cls')

a = "Ivo"
b = 39.9
c = 1981
d = "Zelić"
e = "1012"

print()
print("\nSve varijable u jednom redu\n")
print(a, b, c, d, e)
print()
print("\nSvaka varijabla u svojem redu\n")
print(a, b, c, d, e, sep='\n')

'''3. Napišite program koji ispisuje niz znakova: "Hello World" te neka se 
na kraj ispisanog niza ispiše i znak "!". Uskličnik funkciji print() 
prenesite kao end argument.'''

print("Hello World", end='!')