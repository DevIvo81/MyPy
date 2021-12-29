'''
1. Zadatak - Iscrtati bor sa razmakom u sredini 
naopako pa normalno

A = 7

******* *******
 ****** ******
  ***** *****
   **** ****
    *** ***
     ** **
      * *
      
'''
import os
os.system('cls')

# KRATKA VERZIJA NAOPAKOG BORA SA 10*

brojac = 0
print('\n\n')
for i in range(10, 0, -1):
    print('*' * i, ' ','*' * i, end='\n')
    brojac += 1
    print(' ' * brojac, end='')


# PUNI KOD S BOROVIMA NA OBJE STRANE I UPITOM OKO ZAVRŠETKA


while True:
    
    os.system('cls')
    
    # a = 'BOR S RAZMAKOM U SREDINI NAOPAKO!'
    # print()
    # print(a)
    # print('_' * len(a) + '\n')
    
    zvijezde = int(input('\nUnesi  broj * '))
    print()
       
    brojac = 0

    for i in range(zvijezde, 0, -1):
        print('*' * i + ' ' + '*' * i, end='\n')
        brojac += 1
        print(' ' * brojac, end='')
   
    cajger = zvijezde

    for j in range(zvijezde+1):
            cajger = zvijezde - j
            print(' ' * cajger, end='')
            print('*' * j + ' ' + '*' * j, end='\n')
            cajger -= 1
            
    if input('\nJoš jednom [Y / N]?  ').lower() =='n':
        print('\nDo sljedećeg puta, pozdrav!')
        break
    