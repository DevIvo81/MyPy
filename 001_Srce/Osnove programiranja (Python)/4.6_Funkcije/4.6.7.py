'''7.  ** Napišite program koji će inicijalizirati u varijable n i m dva cijela 
broja proizvoljnih vrijednosti. Provjerite zadovoljavaju li inicijalizirane 
vrijednosti uvjet: 0 ≤ n ≤ m. Ako uvjet nije zadovoljen, tada ispišite 
poruku: "Nedozvoljene vrijednosti!". Ako je uvjet zadovoljen 
izračunajte i ispišite binomni koeficijent "m povrh n", pri čemu 
koristite sljedeći izraz:

(𝑚) =   _____𝑚!______ 
(𝑛)      𝑛! ∗ (𝑚 − 𝑛)!

Primjer: 5! se izračunava na način 5*4*3*2
(Napomena: Implementirajte funkciju fakt(), tako implementirana 
funkcija izračunava faktorijele, na primjer, za poziv funkcije 
fakt(5), povratna vrijednost je: 120. Funkcija se mora pozivati iz 
glavnog programa za sve 3 vrijednosti: m!,  n!,  (m-n)!)
'''
import os
os.system('cls')

def fakt(x):
    f = 1
    for i in range(x, 0, -1):
        f *= i
    return f
            

while True:

    m = int(input("\nUpiši broj 'm': "))
    n = int(input("\nUpiši broj 'n': "))
    print("\n", m, "! = ", fakt(m))
    print("\n", n, "! = ", fakt(n))
    binko = 1
    if not 0<=n<=m:
        print("\nNedozvoljene vrijednosti!\n")
    else:
        binko = fakt(m) / (fakt(n) * fakt(m-n))
        print("\nBinomni koeficijent brojeva 'm i 'n'  m! / n!*(m-n)!  iznosi", binko)
    
    if input("\nJoš jedna runda? [Y/N] ").upper() == 'N':
        break