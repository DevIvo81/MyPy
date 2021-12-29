'''
Imate 10000 kn i možete zaboraviti na njih na 15 godina. 
Ako Vam banka nudi 2.5% godišnju kamatu za taj iznos, 
koliko ćete zaraditi nakon 15 godina. 

Jednostavni kamatni račun k = C * p * t
k = iznos kamata odnosno prinos
C = iznos glavnice
p = godišnja kamatna stopa – NAPOMENA: 5% = 5 / 100 = 0.05
t = vrijeme u godinama
'''

# glavnica = 10000
glavnica = int(input('Upiste iznos glavnice '))

# vrijeme = 35
vrijeme = int(input('Upisite trajanje stednje u godinama '))

# godisnja_kamatna_stopa = (2.5 / 100) # 0.025
godisnja_kamatna_stopa = int(input('Upisite postotak godisnje kamate '))
godisnja_kamatna_stopa = godisnja_kamatna_stopa / 100
# godisnja_kamatna_stopa /= 100

kamata = glavnica * godisnja_kamatna_stopa * vrijeme

# rjesenje = print('Nakon 15 godina zarada je: ', kamata, 'kn')
# rjesenje1 = ''
print('Nakon', vrijeme, 'godina zarada je: ', kamata, 'kn')

print()
# print(rjesenje)