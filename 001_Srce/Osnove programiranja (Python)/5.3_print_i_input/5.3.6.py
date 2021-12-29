'''6.  Učitavajte brojeve koji predstavljaju dobiveni broj bodova na ispitu. 
Za broj bodova [0,50>, ispišite "Nedovoljan!", za broj bodova [50, 
62.5> ispišite "Dovoljan!", za broj bodova [62.5, 75> ispišite "Dobar!", 
za broj bodova [75, 87.5> ispišite "Vrlo dobar!", a za broj bodova 
[87.5, 100] ispišite "Odličan!". U slučaju da je uneseni broj izvan 
raspona brojeva <0, 100>, ispišite prikladnu poruku i prekinite daljnje 
učitavanje broja bodova.'''

import os
os.system('cls')

c = 0
while c < 10:
    
    bodovi = float(input("\n Upiši broj bodova na ispitu: "))

    if 0<=bodovi<50:
        print("\nNEDOVOLJAN!\n")
    elif 50<=bodovi<62.5:
        print("\nDOVOLJAN!\n")
    elif 62.5<=bodovi<75:
        print("\nDOBAR!\n")
    elif 75<=bodovi<87.5:
        print("\nVRLO DOBAR!\n")
    elif 87.5<=bodovi<=100:
        print("\nODLIČAN!\n")
       
