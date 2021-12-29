'''5.  Pozovite funkciju koja ne prima nijedan parametar, ali mora 
izračunati i ispisati zbroj dvaju brojeva. Brojevi neka se dohvate iz 
glavnog dijela programa preko globalnih varijabli.
6.  Prethodni zadatak napišite, a da ne koristite globalne varijable 
(korištenjem parametara funkcije).'''

import os
os.system('cls')

def suma():
    print("Suma brojeva ", a, " i ", b, "iznosi ==",a+b)
a = 5
b = 10
suma()

def suma1(a,b):
    a = 5
    b = 10
    print("Suma brojeva ", a, " i ", b, "iznosi ==",a+b)
suma1(a, b)



