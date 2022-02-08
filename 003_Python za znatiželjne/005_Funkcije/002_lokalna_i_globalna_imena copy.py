import os
os.system('cls' if os.name == 'nt' else 'clear')

def srednja_vrijednost(lista_brojeva):  # lista_brojeva je FORMALNI ARGUMENT
    print(sum(lista_brojeva) / len(lista_brojeva))

moje_ocjene = [2, 3, 2, 4]  # lista u glavnom kodu gdje pozivamo funkciju je STVARNI ARGUMENT

srednja_vrijednost([2, 3, 2, 4])
srednja_vrijednost([1] + [2, 3])
print([1] + [2, 3])

def potenciraj(lista_brojeva, potencija):
    for broj in lista_brojeva:
        print(broj ** potencija)
        
brojevi = [range(1,6)]

potenciraj(list(range(1,6)), 3)

print('\n')