import os
os.system('cls')
'''
Klasa TV aparat: širina, visina, dijagonala
...

Funkcije: Uključi TV; Promijeni program; Namjesti glasnoću

'''

class TelevizijskiAparat:
    """Najmoderniji TV Aparat na svijetu"""
    def __init__(
        self, dijagonala, sirina, visina, proizvodac, model, je_ukljucen,
        program = 1, glasnoca = 10
    ):
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.je_ukljucen = je_ukljucen
        self.program = program
        self.glasnoca = glasnoca
    
    def ukljuci_tv(self):
        self.je_ukljucen = True
        self.glasnoca = 5
        self.program = 2
    
    def promijeni_program(self, novi_program):
        self.program = novi_program
    
    def podesi_glasnocu(self, smjer_glasnoce = ' ', razina_glasnoce = 1):
            if smjer_glasnoce == 'glasnije':
                self.glasnoca +=1
            elif smjer_glasnoce == 'tise':
                self.glasnoca -= 1
            elif smjer_glasnoce == 'prigusi':
                self.glasnoca = 0

tv_salon = TelevizijskiAparat(55, 150, 76, 'Philips', 'XYZWQ', False)
tv_db = TelevizijskiAparat(78, 250, 96, 'Grundig', 'WQXYZ', True, glasnoca=25)
print()
print(tv_salon.proizvodac)
print(tv_salon.glasnoca)
print()
print(tv_db.proizvodac)
print(tv_db.glasnoca)
print('\n')

tv_salon.ukljuci_tv()
tv_db.ukljuci_tv()

print()
print(tv_salon.proizvodac)
print(tv_salon.glasnoca)
print(tv_salon.program)
print()
print(tv_db.proizvodac)
print(tv_db.program)
print('\n')

tv_salon.promijeni_program(50)
tv_salon.podesi_glasnocu('glasnije')

print()
print(tv_salon.proizvodac)
print(tv_salon.program)
print(tv_salon.glasnoca)
print()
print(tv_db.proizvodac)
print(tv_db.program)
print('\n')


'''
tv_dnevni_boravak = TelevizijskiAparat()

print(f'Status oba TV aparata')

print('Uključi TV u salonu')
tv_dnevni_boravak.ukljuci_tv()

if tv_dnevni_boravak.je_ukljucen:
    print(f'TV u DB JE UKLJUČEN')
    tv_dnevni_boravak.ukljuci_tv()
else:
    print('TV u DB JE UKLJUČEN')

if tv_salon.je_ukljucen:
    print(f'TV u salonu JE UKLJUČEN')
else:
    print('TV u salonu NIJE UKLJUČEN')
    

'''