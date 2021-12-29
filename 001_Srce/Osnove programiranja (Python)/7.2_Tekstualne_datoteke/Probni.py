import os
os.system('cls')
# 1. PODACI O OSOBI U VARIJABLAMA
'''
first_name = 'Ivo'
last_name = 'Ivic'
dob = "10th December, 1981."
country = "Hrvatska (Croatia)"
employment_status = 'Nezaposlen'
body_weight = 94
gender = "muški"
print('\n', first_name, last_name, dob, country,
employment_status, body_weight, gender) # ispis svih varijabli u jednom retku
print('\n', first_name, last_name, dob, country,
employment_status, body_weight, gender, sep='\n') # ispis svake varijable u zasebnom retku
'''
# 2. STRANICE I POVRŠINA ČETVEROKUTA
'''
a = int(input('\nUnesi stranicu "a": '))
b = int(input('\nUnesi stranicu "b": '))
area = a * b
print('\nPovršina četverokuta stranica "a" i b" iznosi ', area)
'''
# 3. STRUJA
'''
base_cost = 0.66 # cijena kWh
total_cost = 0
total_consum = 0
appliances = []
c = ''
# broj = int(input('Unesi broj uređaja za koje želiš izračunati potrošnju el. energije: '))
broj = 1
for i in range(broj):
# app_name = input('\nUpiši ime uređaja: ').capitalize()
app_name = 'Mikrovalna pećnica'
# wattage = float(input('\nUpiši snagu uređaja u "kW": '))
wattage = 1.3
# day_time_on = float(input('\nUpiši dnevni broj sati rada: '))
day_time_on = 2
month_time_on = day_time_on * 30
day_consum = wattage * day_time_on
day_cost = base_cost * day_consum
month_consum = day_consum * 30
month_cost = month_consum * base_cost
print('\nUređaj: ', app_name,
'\nSnaga: ', wattage, ' kw ',
'\nDnevni broj sati rada: ', day_time_on,
'\nMjesečni broj sati rada: ', month_time_on,
'\nDnevna potrošnja: ', round(day_consum, 2), 'kWh',
'\nDnevna cijena: ',round(day_cost, 2), ' HRK ',
'\nMjesečna potrošnja: ', round(month_consum, 2), 'kWh',
'\nMjesečna cijena: ', round(month_cost, 2), 'HRK')
total_consum += month_consum
total_cost += month_cost
c += app_name
appliances.append(app_name)
print()
print('#'*len(c))
print()
print(*appliances, sep=', ')
print()
print('#'*len(c))
print('\nUkupna mjesečna potrošnja: ', round(total_consum,2), 'kWh',
'\nUkupna cijena: ', round(total_cost, 2), 'HRK')
'''
# 4. TROKUT
'''
# da pojednostavnimo priču uzet ćemo pravokutni trokut,
# gdje je visina stranice "a" iste duljine kao kateta "b".
a = 3
b = 4
c = 5
o = a + b + c
Va = b
p = a * Va / 2
print('\nPRAVOKUTNI TROKUT\n')
print('\nStranica a = ', a, 'cm')
print('Stranica b = ', b, 'cm')
print('Stranica c = ', c, 'cm')
print('\nOpseg O = ', o, 'cm')
print('\nVisina Va = ', Va, 'cm')
print('\nPovršina P = ', round(p), 'cm2')
'''