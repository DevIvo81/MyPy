import os, time, locale
import datetime as dt
locale.setlocale(locale.LC_ALL, 'hrv')

#region SAT I DATUM
'''
def točno_vrijeme():
    
    datum = dt.date.today()
    
    sada = dt.datetime.now()
    datum_i_vrijeme = f'\n{sada.strftime("%B")}\t{sada.strftime("%d.%m.%Y. %H:%M:%S")}'
    print(datum_i_vrijeme)
    

    
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    točno_vrijeme()

    time.sleep(1)
'''
#endregion



#region KOCKICA

def kocka():
    from random import randint as rnt
    print(f'\nRezultat = {rnt(1,6)}')


os.system('cls' if os.name == 'nt' else 'clear')
    
for i in range(10):
    kocka()



#endregion