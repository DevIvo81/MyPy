'''
Evidencija Kupaca i Djelatnika Firme
Osoba
    Fizička osoba (Kupac)
    Pravna osoba (Kupac)

Kupac - fizicka i pravna osoba
Djelatnik firme - fizicka osoba
Firma - pravna osoba
Firma ima djelatnike
Kupac (pravna osoba) ima kontakt - fizicka osoba
'''

class Osoba:
    def __init__(self, oib, adresa, email, mobitel):
        self.ime = ''
        self.oib = self.get_data_from_DB()
        self.adresa = adresa
        self.email = email
        self.mobitel = mobitel

        #self.get_data_from_DB()

    def get_data_from_DB(self):
        # spoji se na bazu
        # dohvati podatke
        # popuni svojstva
        pass

    def ispis(self):
        print()
        print(self.ime)
        print(self.oib)
        print(self.adresa)
        print(self.email)
        print(self.mobitel)
        print('\n')


class Tvrtka(Osoba):
    def __init__(self, ime, oib, adresa, email, mobitel,
                djelatnost, djelatnici, tip):
        super().__init__(ime, oib, adresa, email, mobitel)
        self.djelatnost = djelatnost
        self.djelatnici = djelatnici
        self.tip = tip # Kupac, Dobavljac, Partner, Podruznica

    def ispis(self):
        super().ispis()
        print(self.djelatnost)
        for djelatnik in self.djelatnici:
            print(djelatnik.ispis())


class Kontakt(Osoba):
    def __init__(self, ime, oib, adresa, email, mobitel,
                prezime, pozicija):
        super().__init__(ime, oib, adresa, email, mobitel)
        self.prezime = prezime
        self.pozicija = pozicija

    def ispis(self):
        #super().ispis()
        print()
        print(f'{self.ime} {self.prezime}')
        print(self.pozicija)
        print(self.oib)
        print(self.adresa)
        print(self.email)
        print(self.mobitel)
        print('\n')


class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, email, mobitel,
                prezime, radno_mjesto):
        super().__init__(ime, oib, adresa, email, mobitel)
        self.prezime = prezime
        self.radno_mjesto = radno_mjesto

    def ispis(self):
        print()
        print(f'{self.ime} {self.prezime}')
        print(self.radno_mjesto)
        print(self.oib)
        print(self.adresa)
        print(self.email)
        print(self.mobitel)
        print('\n')



def kreiraj_djelatnika():
    ime = input('Upisite ime osobe: '),
    prezime = input('Upisite prezime osobe: '),
    oib = input('Upisite OIB osobe: '),
    adresa = input('Upisite adresu osobe: '),
    email = input('Upisite email osobe: '),
    mobitel = input('Upisite mobitel osobe: '),
    radno_mjesto = input('Upisite naziv radnog mjesta: ')        

    return Djelatnik(ime, oib, adresa, email, 
                mobitel, prezime, radno_mjesto)


def kreiraj_tvrtku():
    naziv = input('Upisite naziv tvrtke: ')
    oib = input('Upisite OIB tvrtke: ')
    adresa = input('Upisite adresu tvrtke: ')
    email = input('Upisite email tvrtke: ')
    mobitel = input('Upisite mobitel tvrtke: ')
    djelatnost = input('Upisite djelatnost tvrtke: ')
    tip = input('Upisite tip tvrtke (Kupac, Dobavljac, Firma): ')
    
    print('UNOS DJELATNIKA/KONTAKATA')
    while True:
        djelatnici.append(kreiraj_djelatnika())
     
        if not input('Novi djelatnik? (da / ne -> ENTER)'):
            break

    return Tvrtka(naziv, oib, adresa, email, 
        mobitel, djelatnost, djelatnici, tip)


# GLAVNI DIO PROGRAMA
kupci = []
djelatnici = []

while True:   
    kupci.append(kreiraj_tvrtku())

    if not input('Nova tvrtka? (da / ne -> ENTER)'):
        break


for kupac in kupci:
    kupac.ispis()

