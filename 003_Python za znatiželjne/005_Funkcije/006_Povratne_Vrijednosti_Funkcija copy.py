import os
os.system('cls' if os.name == 'nt' else 'clear')

def srednja_vrijednost(lista):
    return sum(lista) / len(lista)

temperature = [28, 29, 26]

sredina = srednja_vrijednost(temperature)

veća_sredina = 1 + srednja_vrijednost(temperature)

def ispitni_odsječak():
    temperature = [28, 29, 26]
    prosjek = srednja_vrijednost(temperature)
    print(prosjek)



