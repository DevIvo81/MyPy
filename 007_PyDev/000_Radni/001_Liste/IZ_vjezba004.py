# KONVERZIJA IP ADRESE

ip_adresa  = '192.168.0.164'
ip_1 = 192
ip_2 = 168
ip_3 = 0
ip_4 = 164

print('\nDekadski oblik: ', ip_1, '.', ip_2, '.', ip_3, '.', ip_4, sep='' )
print('\nBinarni oblik: ', bin(ip_1), '.', bin(ip_2), '.', bin(ip_3), '.', bin(ip_4), sep='' )
print('\nHeksadekadski oblik: ', hex(ip_1), '.', hex(ip_2), '.', hex(ip_3), '.', hex(ip_4), sep='' )
print('\nOktalni oblik: ', oct(ip_1), '.', oct(ip_2), '.', oct(ip_3), '.', oct(ip_4), sep='' )
input('\n')

# Iz ... natrag u dekadski - int('broj_za_konverziju, baza)
# baza = 2(bin), 8(oct), 16(hex) -- default je 10

binarni = 110011
binarni_string = str(binarni)
dekadski = int(binarni_string, 2)
print(dekadski)