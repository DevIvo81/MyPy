'''
Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at 
the 3rd position of the array, the sum of left side 
of the index ({1,2,3}) and the sum of the right side 
of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at 
the 1st position of the array, the sum of left side 
of the index ({1}) and the sum of the right side of 
the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. 
(Empty arrays are equal to 0 in this problem)

Index 0 is the place where the left side and right side are equal.
'''

import os
from random import randint as rnt
os.system('cls')

def find_even_index(a):
    
    flag = [i for i in range(len(a)) if sum(a[ : i]) == sum(a[i+1 : ])]
    
    return flag[0] if flag else -1
       
        
print(find_even_index([1,100,50,-51,1,1]),1)
print()
print(find_even_index([1,2,3,4,3,2,1]),3)
print()
print(find_even_index([1,100,50,-51,1,1]),1,)
print()
print(find_even_index([1,2,3,4,5,6]),-1)
print()
print(find_even_index([20,10,30,10,10,15,35]),3)
print()
print(find_even_index([20,10,-80,10,10,15,35]),0)
print()
print(find_even_index([10,-80,10,10,15,35,20]),6)
print()
print(find_even_index(list(range(1,100))),-1)
print()
print(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
print()
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
print()
print(find_even_index(list(range(-100,-1))),-1)
print()
