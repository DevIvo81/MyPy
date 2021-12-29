'''
Izračun mjesečne potrošnje el. struje te
cijene el. struje koju potroši mikrovalna 
pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
'''

microwave_power = 1.3 # kW
daily_usage = 2 # h
monthly_usage = daily_usage * 30 # pretpostavka 30 dana/mj.
# monthly_usage = daily_usage * (365 / 12)
el_price = 0.95 # kn / 1 kWh
el_price_w_tax = el_price * 1.25 # PDV 25% 

el_usage = microwave_power * monthly_usage # kW * h

microwave_cost = el_usage * el_price
microwave_cost_w_tax = el_usage * el_price_w_tax


print('Mjesecni trosak mikrovalne pecnice je:', microwave_cost,'kn')
print('Mjesecni trosak mikrovalne pecnice s PDV-om je:', microwave_cost_w_tax,'kn')