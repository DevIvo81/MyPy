import os
from random import randint as rnt

os.system('cls')

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
    
        

brojevi = [rnt(1, 999) for i in range(8)]    

print(brojevi)

brojevi.sort()

print(brojevi)

print(sum_two_smallest_numbers(brojevi))