'''8.  * Napravite rječnik proizvoljnog sadržaja sljedećeg oblika: 
povrce = {'krumpir' : ['bijeli', 'crveni', 'za salatu'], 
        'luk' : ['bijeli', 'crveni']}
Za svaki tip povrća ispišite broj pripadajućih vrsti. Sadržaj ispisa 
(temeljen na gornjem primjeru) neka bude:
Krumpir : 3 
Luk : 2
Primijetite da riječi Krumpir i Luk počinju velikim početnim 
slovom, dok su u rječniku napisane kompletno malim slovima.'''
import os
os.system('cls')

povrce = {'krumpir' : ['bijeli', 'crveni', 'za salatu'], 
        'luk' : ['bijeli', 'crveni']}

for vrsta in povrce.keys():
    print(vrsta.title(), ':', len(povrce[vrsta]))



