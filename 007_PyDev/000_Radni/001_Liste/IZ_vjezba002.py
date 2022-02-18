import os
os.system('cls')

fuel = 5.3  # litara / 100 km
price = 11.17 
one_km = fuel / 100
days = 30
one_dir_dist = 20 # dnevni put u jednom smjeru

daily_cost = price * one_km * one_dir_dist * 2

monthly_cost = daily_cost * 30

print('\nAko dnevno prelazi 20 km do posla i nazad ')
print('dnevno to iznosi:\t', one_dir_dist * one_km * 2, '\tlitara goriva')
print('\nCijena po danu je:\t', daily_cost)
print('\na mjesečno to iznosi:\t', monthly_cost)

### KAMATE

principal = 10000
period = 15
interest = 0.025
total = principal * period * interest
print('\nNakon ', period, ' godina, uz kamatu od 2.5%, ')
print('na uloženih', principal, ' iznos zarade je: ', total, 'HRK\n')

