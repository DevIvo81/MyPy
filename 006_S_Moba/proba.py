import os, random, string
os.system('cls')

digSum = 0
x = 4096
while x > 0:
    print(x%10, end =' + ')
    digSum += (x % 10)
    x //= 10

print()
if (x**(1/2)).is_integer() and digSum <= 20
: 
    print(f'\nSum of digits is {digSum}')