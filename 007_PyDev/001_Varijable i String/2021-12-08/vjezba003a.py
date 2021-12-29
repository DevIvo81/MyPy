'''
IP adresu iz primjera ispišite u binarnom, oktalnom i 
heksadekadskom obliku.
SAVJET: Za sada koristite zasebnu varijablu za svaki 
od četiri broja, odnosno dijela (okteta) IP adrese, 
ali ispišite ih u istom obliku kako je navedeno u primjeru 
(192.168.0.184).
Ispis treba napraviti za sve oblike brojevnih sustava.
'''

ip_adresa = '192.168.0.164'
ip_1 = 192
ip_2 = 168
ip_3 = 0
ip_4 = 164

ip_1_bin = bin(ip_1)
ip_2_bin = bin(ip_2)
ip_3_bin = bin(ip_3)
ip_4_bin = bin(ip_4)

ip_1_hex = hex(ip_1)
ip_2_hex = hex(ip_2)
ip_3_hex = hex(ip_3)
ip_4_hex = hex(ip_4)


print('Dekadski oblik: ', ip_1, '.', ip_2, '.', ip_3, '.', ip_4, sep='')
print('Binarni oblik: ', ip_1_bin, '.', ip_2_bin, '.', ip_3_bin, '.', ip_4_bin, sep='')
print('Heksadekaski oblik: ', ip_1_hex, '.', ip_2_hex, '.', ip_3_hex, '.', ip_4_hex, sep='')

binarni = 110011
binarni_string = str(binarni)

dekaski = int(binarni_string, 2)

print('Dekadski oblik 110011: ', dekaski)

'''
Iz dekadskog u binarni – bin(cijeli_broj_koji_konvertiramo)
Iz dekadskog u oktalni – oct(cijeli_broj_koji_konvertiramo)
Iz dekadskog u heksadekadski – hex(cijeli_broj_koji_konvertiramo)
Iz … natrag u dekadski – int('broj_koji_konvertiramo', baza)
'''