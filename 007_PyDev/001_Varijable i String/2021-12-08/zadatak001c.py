'''
Stranice trokuta, povrΕ‘inu trokuta 
(P = (π β π£_π)/2, π£_π je visina na stranicu a) 
te opseg trokuta.
'''

a = 3.5
v_a = 4

p_trokuta = (a * v_a) / 2

b_kvadrat = v_a ** 2 + (a / 2) ** 2
b = b_kvadrat ** (1 / 2)

print('A stranica trokuta je:', a)
print('B stranica trokuta je:', b)
print('Visina trokuta na stranicu a je:', v_a)
print('Povrsina trokuta je:', p_trokuta)