# IP adrese: 192.168.0.184
# #EA-43-35 (234, 67, 53)

dio_1 = 192
dio_2 = 168
dio_3 = 0
dio_4 = 184

dio_1_bin = bin(dio_1)
dio_2_bin = bin(dio_2)
dio_3_bin = bin(dio_3)
dio_4_bin = bin(dio_4)

print(dio_1, '.', dio_2, '.', dio_3, '.', dio_4)
print(dio_1_bin, '.', dio_2_bin, '.', dio_3_bin, '.', dio_4_bin)
print()


red_hex = 'EA'
green_hex = '43'
blue_hex = '35'

red_dec = int(red_hex, 16)
green_dec = int(green_hex, 16)
blue_dec = int(blue_hex, 16)

print(red_hex, ' ', red_dec)
print(green_hex, ' ', green_dec)
print(blue_hex, ' ', blue_dec)