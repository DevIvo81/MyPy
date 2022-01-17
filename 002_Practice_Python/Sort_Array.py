'''
Task
You will be given an array of numbers. 
You have to sort the odd numbers in 
ascending order while leaving the even 
numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

'''



import os
from random import randint as rnt
os.system('cls')

def sort_array(a):
    
    noviNiz = []
    neparni = []
    
    for i in a:
        if i % 2 == 0:
            noviNiz.append(i)
        else:
            noviNiz.append('#')
            neparni.append(i)
    
    neparni.sort()
    print()
    print(noviNiz)
    print()
    print(neparni)
    print()
    
    while neparni:
        for broj in noviNiz:
            if broj == '#':
                stash = broj
                novi = neparni.pop(0)
                broj = novi
    
    print(noviNiz)
    print()
    
    l = len(a)
    # for i in range(l):
    #     for j in range(l-1):
    #         if a[j] > a[j+1] and a[j] % 2 !=0:
    #             temp = a[j]
    #             a[j] = a[j+1]
    #             a[j+1] = temp
    # return(noviNiz)



niz = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(niz)
print()

sort_array(niz)
print()
# print(sort_array(niz))
# print()

