import os
os.system('cls')

carsList = [\
    {
'make' : 'Toyota', 'model' : 'Prius', 'year' : 2006, 'color' : 'gold', 'doors' : 4,
'leather' : False, 'license' : 'ABC123', 'mileage' : 777777},\
    {
'make' : 'Honda', 'model' : 'Civic', 'year' : 2010, 'color' : 'red', 'doors' : 2,
'leather' : False, 'license' : 'DEF444', 'mileage' : 54321},\
    {
'make' : 'Ford', 'model' : 'Fusion', 'year' : 2012, 'color' : 'blue', 'doors' : 4,
'leather' : True, 'license' : 'GHI999', 'mileage' : 24680},\
    {
'make' : 'Chevrolet', 'model' : 'Volt', 'year' : 2015, 'color' : 'black', 'doors' : 4,
'leather' : False, 'license' : 'JKL444', 'mileage' : 7890},\
    {
'make' : 'Toyota', 'model' : 'Prius', 'year' : 2006, 'color' : 'gold', 'doors' : 4,
'leather' : False, 'license' : 'ABC123', 'mileage' : 777777},\
    ]

for carDict in carsList:
    if carDict['doors'] == 4 and carDict['mileage'] < 50000:
        print(carDict['make'], carDict['model'], carDict['license'])