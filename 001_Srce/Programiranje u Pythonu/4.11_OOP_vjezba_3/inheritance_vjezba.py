import os
os.system('cls' if os.name == 'nt' else'clear')
'''
#region OSOBA

class Osoba:
    
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        
    def ispis(self):
        print('\nOSOBA\n')
        print(f'IME:\t{self.ime}')
        print(f'PREZIME:\t{self.prezime}')
        
    def hodaj(self):
        print(f'\nHODAM!')
        

class Zaposlenik(Osoba):
    
    def __init__(self, ime, prezime, placa):
        super().__init__(ime, prezime)
        self.placa = placa
    
    def info_Zaposlenik(self):
        print('\nZAPOSLENIK\n')
        print(f'IME:\t{self.ime}')
        print(f'PREZIME:\t{self.prezime}')
        print(f'PLAĆA:\t{self.placa}')
    
    def naplati(self):
        print('\nNAPLAĆUJEM!')
    

class Kupac(Osoba):
    
    def __init__(self, ime, prezime, tip_kupca):
        super().__init__(ime, prezime)
        self.tip_kupca = tip_kupca
        
    def info_Kupac(self):
        print('\nKUPAC\n')
        print(f'IME:\t{self.ime}')
        print(f'PREZIME:\t{self.prezime}')
        print(f'TIP KUPCA:\t{self.tip_kupca}')
    
    def kupi(self):
        print('\nKUPUJEM!')
        

o = Osoba('Ivo', 'Zelić')
o.ispis()
o.hodaj()

z = Zaposlenik('Ana', 'Cigula', 9000)
z.info_Zaposlenik()
z.ispis()
z.hodaj()
z.naplati()

k = Kupac('Ante', 'Zelić', 'Fizički kupac')
k.info_Kupac()
k.ispis()
k.hodaj()
k.kupi()

#endregion
'''


'''
#region OVERLOADING

class Demo:
    
    def metoda(self, param1=None, param2=None):
        
        if param1 is None and param2 is None:
            print('Metoda bez parametara!')

        elif param2 is None:
            print(f'Parametar: {param1}')
            
        else:
            print(f'Parametri: {param1} i {param2}')

d = Demo()
d.metoda()
d.metoda('A')
d.metoda('A', 'B')

#endregion

'''


#region OVERRIDING

class Osoba:
    
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        
    def ispis(self):
        print(f'\nJa sam {self.ime} {self.prezime}\n')

class Zaposlenik(Osoba):
    
    def __init__(self, ime, prezime, placa):
        super().__init__(ime, prezime)
        self.placa = placa
    
    def ispis(self):
        print(f'IME: {self.ime}')
        print(f'PREZIME: {self.prezime}')
        print(f'PLAĆA: {self.placa}')
        print()
        
z = Zaposlenik('Ana', 'Zelić', 9000)

z.ispis()