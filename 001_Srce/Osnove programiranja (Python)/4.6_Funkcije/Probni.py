import os
os.system('cls')

x = 5
p = 1

for i in range(5, 0, -1):
    p *= i
    print(i, end=' ')
print(p)