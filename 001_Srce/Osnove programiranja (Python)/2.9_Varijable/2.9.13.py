# spajanje, ponavljanje, dohvaćanje vrijednosti na indeksu,
# vraćanje dijela niza omeđenog indeksima, provjera znaka u nizu,
# provjera NE nalazi li se znak u nizu
import os
os.system('cls')

a = "Dark"
b = "Souls"

print()
print(a, b, sep =' ')
print()
print("\nSpajanje == ", a+b)
print("\nPonavljanje == ", a*2, b*2)
print("\nDohvaćanje k i S == ", a[3], b[0])
c=a+b
print("\nVraćanje dijela spojenog niza == ", c[3:8])
print("\nProvjera da li je 'a' u nizovima == ", "a" in a, "a" in b)
print("\nProvjera da li 's' NIJE u nizovima == ", "s" not in a, "s" not in b)