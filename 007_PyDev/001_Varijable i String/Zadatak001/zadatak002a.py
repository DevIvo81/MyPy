'''
Ako automobil troši 5.3 litara na 100 km 
i ako je cijena goriva 9.56 kn po litri 
(nije važno kojeg goriva), 
izračunajte koliko košta 1 km vožnje automobilom. 
Prikažite mjesečni trošak (30 dana) odlaska na 
posao automobilom koji je udaljen 20 km u jednom smjeru.
'''

# Potrosnja na 100 km
potrosnja_automobila_100 = 5.3 
# Potrosnja na 1 km
potrosnja_automobila_1 = potrosnja_automobila_100 / 100

cijena_goriva = 11.3
cijena_1km_voznje = potrosnja_automobila_1 * cijena_goriva

print('Cijena 1 km voznje iznosi:', cijena_1km_voznje, 'kn')


udaljenost_do_posla = 20
ukupna_udaljenost = udaljenost_do_posla * 2
broj_radnih_dana = 30 # 21

cijena_odlaska_na_posao = ukupna_udaljenost * cijena_1km_voznje * broj_radnih_dana

print('Mjesecni trosak odlaska na posao je:', cijena_odlaska_na_posao, 'kn')
