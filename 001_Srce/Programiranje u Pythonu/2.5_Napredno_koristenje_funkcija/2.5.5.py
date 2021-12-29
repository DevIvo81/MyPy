'''5.  Isprobajte korištenje ugniježđenih funkcija. Vanjska funkcija 
imena izracun() neka prima dva parametra. Unutar vanjske funkcije 
kreirajte dvije unutarnje funkcije imena parniZbroj() i 
neparniZbroj(). Funkcija parniZbroj() neka vraća rezultat 
matematičke formule 2*a+5*b, a funkcija neparniZbroj() 
neka vraća rezultat matematičke formule a*b-10. Koja će se od 
dviju kreiranih unutarnjih funkcija pozvati neka se odredi na 
temelju parnosti zbroja primljenih parametara a+b. U glavnom 
programu na zaslon ispišite rezultat.'''
import os
os.system('cls')

a = input('\nUpiši broj "a": ')
a = int(a)
b = input('\nUpiši broj "b": ')
b = int(b)

def izracun(a, b):
    
    def parniZbroj(a, b):
        return 2*a + 2*b
    
    def neparniZbroj(a, b):
        return a*b - 10

    if (a + b) % 2 == 0:
        f = parniZbroj(a, b)
        return print(f'\nSuma brojeva {a} i {b} je parna pa je 2*a + 2*b = {f}')
        
    else:
        f = neparniZbroj(a, b)
        return print(f'\nSuma brojeva {a} i {b} je neparna pa je a*b - 10 = {f}')

izracun(a, b)

    