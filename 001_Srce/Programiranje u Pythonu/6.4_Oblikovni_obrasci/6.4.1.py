import os
os.system('cls' if os.name == 'nt' else 'clear')

'''
1.  Napišite programski kôd koji će omogućiti generiranje 
    nasumičnih brojeva na način opisan u nastavku. Početna, tj. prva 
    vrijednost koja se mora vratiti jest 67, a svaka sljedeća vrijednost 
    računa se na temelju sljedeće formule:
    9845612 % prethodna_vrijednost  + 17 *  7

    Pomoću oblikovnog obrasca "jedinstveni objekt" osigurajte samo 
    jedno instanciranje objekta unutar kojeg će biti pohranjena 
    prethodno generirana vrijednost. Unutar razreda imena 
    NasumicniBroj implementirajte metodu imena sljedeci(), 
    kod svakog njezinog poziva ta metoda vraća novu vrijednost 
    dobivenu na temelju gore napisane formule. Primijetite da će 
    generirane vrijedosti biti identične svaki put kada se programski 
    kôd pokrene ponovo.
'''

class Nasumicni_Broj:
    __singleton = None
    
    def __init__(self):
        if Nasumicni_Broj.__singleton is None:
            Nasumicni_Broj.__singleton = self
            Nasumicni_Broj.__sljedeci = 67
        else:
            raise Exception("Singleton!")
    
    @staticmethod
    def get_instance():
        if Nasumicni_Broj.__singleton is None:
            Nasumicni_Broj()
        return Nasumicni_Broj.__singleton
    
    def sljedeci(self):
        x = self.__sljedeci
        self.__sljedeci = 9845612 % x + 17 * 7
        return x
    
g1 = Nasumicni_Broj.get_instance()
g2 = Nasumicni_Broj.get_instance()

print(g1.sljedeci())
print(g2.sljedeci())
print(g1.sljedeci())
print(g2.sljedeci())
print(g1.sljedeci())
print(g2.sljedeci())
print(g1.sljedeci())
print(g2.sljedeci())

    