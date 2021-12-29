'''
1. ZADATAK - JEDNOSTAVNI KALKULATOR
'''

while True:

    import os
    os.system('cls')


    print('_________________________')
    print('|  -  |  +  |  *  |  /  |')
    print('|_____|_____|_____|_____|')
    print('|  7  |  8  |  9  |  %  |')
    print('|-----------------|-----|')
    print('|  4  |  5  |  6  | / / |')
    print('|-----------------|-----|')
    print('|  1  |  2  |  3  | * * |')
    print('|-----------------|-----|')
    print('|     0     |  ,  |  =  |')
    print('|___________|_____|_____|')

    a = float(input('\nUpiši prvi broj: '))
    b = float(input('\nUpiši drugi broj: '))

    op = input('\nUpiši koju operaciju želiš izvršiti [ + , - , * , / , % , //, ** ]:  ')

    if op == '/':
        if b == 0:
            print('\nDijeljenje s nulom nije dopušteno! Pokušaj opet.')
        else: 
            print(f'\nKvocijent brojeva {a} / {b} = {a / b}')
        
    if op == '%':
        if b == 0:
            print('\nDijeljenje s nulom nije dopušteno! Pokušaj opet.')
        else: 
            print(f'\nCjelobrojni ostatak dijeljenja (modulo) brojeva {a} % {b} = {a % b}')
            
    if op == '//':
        if b == 0:
            print('\nDijeljenje s nulom nije dopušteno! Pokušaj opet.')
        else: 
            print(f'\nCjelobrojno dijeljenje brojeva {a} // {b} = {a // b}')
    
    if op == '+':
        print(f'\nZbroj brojeva {a} + {b} = {a + b}')
    
    if op == '-':
        print(f'\nRazlika brojeva {a} - {b} = {a - b}')
    
    if op == '*':
        print(f'\nProdukt brojeva {a} * {b} = {a * b}')
        
    if op == '**':
        print(f'\nPoteciranje brojeva {a} ** {b} = {a ** b}')
        
    if input('\nJoš jednom [Y / N]?  ').lower() =='n':
        print('\nDo sljedećeg puta, pozdrav!')
        break 
    
    
        
