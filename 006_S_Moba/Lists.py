import os, random, string
os.system('cls')







'''
# 11. NUMBERS IN RANGE THAT ARE PERFECT SQUARES
#     WITH SUM OF DIGITS < 10

perfectSquares =[]

for b in range(1, 22202):
    
    digSum = 0
    x = b
    while x > 0:
        digSum += (x % 10)
        x //= 10
           
    if (b**(1/2)).is_integer() and digSum < 10:
        perfectSquares.append(b)

print(f'Perfect squares with sum of digits less than 10 are:',
      f'\n\n{perfectSquares}')


# 10 GENERATING LIST OF TUPLE PAIRS (num, square of num)

print([(i, i ** 2) for i in range(100)])

#print(*[(i, i ** 2) for i in range(21)], sep='\n')

    

# 9. INTERSECTION OF TWO LISTS

a = [random.randint(1,9) for i in range(3)]
b = [random.randint(1,9) for i in range(5)]
a = [5, 4, 6]
b = [4, 3, 5, 1, 9]

i_list = []

for i in a:
    if i in b:
        i_list.append(i)

print(f'\nIntersection of lists is\n\n\t{i_list}')

# 8. UNION OF TWO LISTS

a = [random.randint(1,9) for i in range(3)]
b = [random.randint(1,9) for i in range(5)]
a = [5, 4, 6]
b = [4, 3, 5, 1, 9]

a.sort()
b.sort()

t = '\nInitial lists'
print(t)
print('-'*len(t))
print(f'\n\t{a}\n\n\t{b}')


a = set(a)
b = set(b)

t = '\nInitial sets'
print(t)
print('-'*len(t))
print(f'\n\t{a}\n\n\t{b}')
#help(set.union)

u = a & b
print(f'\nUnion of sets is\n\n\t{u}')


a = [4, 5, 6]
b = [1, 3, 4, 4, 9]

a.sort()
b.sort()

t = '\nInitial lists'
print(t)
print('-'*len(t))
print(f'\n\t{a}\n\n\t{b}')


u = []
for i in a:
    if i not in u:
        if i not in b:
            u.append(i)
        else:
            u.append(i)

for j in b:
    if j not in u:
        if j not in a:
            u.append(j)
        else:
            u.append(j)
u.sort()
print(f'\nUnion of lists is\n\n\t{u}')        




# 7. SORT A LIST ACCORDING TO LENGTH OF ELEMENTS

# a = [input('\nEnter something: ') for i in range(6)]

#a = ['Jadranka', 'Ana', 'Zelic', 'Ante', 'Python', 'Program']
a = ['666666', '22', '4444', '333', '55555', '1']

print(f'\nInitial list\t\t\t\t{a}')

l = len(a)

for i in range(l):
    for j in range(l-1):
        if len(a[j])>len(a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(f'\nList sorted by length of elements\t{a}')
            
    


# 6. FIND THE SECOND LARGEST NUMBER IN LIST USING BUBBLE SORT

n = int(input('Enter number of random list integers: '))
#n = 30

a = [random.randint(1,99) for i in range(n)]
print(f'\n\nList of integers\t\t{a}')
l = len(a)
for i in range(l):
    for j in range(l-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(f'\n\nBubble sorted list of integers\t{a}')
print(f'\nSecond largest number is {a[-2]}')




# 5. SORT THE LIST ACCORDING TO THE SECOND ELEMENT IN SUBLIST PAIRS

n = int(input('\nEnter number of random list pairs: '))
#n = 6

p = [[random.choice(string.ascii_uppercase), random.randint(1, 99)] for i in range(n)]


print(f'\n\nInitial pairs list\t{p}')

p_length = len(p) # number of elements

c = 0

while True : # listing loop - do this for number of elements in the list...
             # ...depending on counter
    stop = True    
    
    for j in range(p_length-1): # (tries - 1) comparison loop i.e 5 elements... 
                                # ...takes 4 comparisons and keeps iterator in range
        if p[j][1] > p[j+1][1]:
            stop = False
            temp = p[j]
            p[j] = p[j+1]
            p[j+1] = temp
    c +=1 
        
    if stop:
        break
    
    print(f'\n{(c+1)-1}. step comparison<-->exchange\t{p}')




# 4. EVEN & ODD LIST ELEMENTS PUT INTO TWO DIFFERENT LISTS

title = 'EVEN & ODD LIST ELEMENTS PUT INTO TWO DIFFERENT LISTS'
print('\n',title)
print('*' * (len(title)+1))

n = int(input('\nEnter number of elements: '))
#n = 20
numbers = [random.randint(1,1000) for i in range(n)]

even_list = []
odds_list = []

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odds_list.append(i)
print(f'\nFrom list of numbers {numbers}'
      f'\n\nEven numbers are {even_list}'
      f'\n\nOdd numbers are {odds_list}')




# 2. & 3 FIND LARGEST AND SECOND LARGEST NUMBER IN LIST

n = int(input('\nEnter number of elements: '))
#n = 15
numbers = [random.randint(1,1000) for i in range(n)]

numbers.sort()

print(f'\n\nList of numbers {numbers}')
print(f'\n\nLargest number in list is {numbers[-1]} and second largest is {numbers[-2]}')




numbers = [random.randint(1,1000) for i in range(n)]

iterlist = []

for i in numbers:
    if i >= largest:
        largest = i
        iterlist.append(largest)

second_largest = iterlist[-2]

print(f'{numbers}\n\nList of largest is {iterlist}\n\nLargest number in list is {largest} and second largest is {second_largest}')




# 1. FIND LARGEST NUMBER IN LIST

numbers = [random.randint(1,1000) for i in range(20)]

largest = 0
smallest = 1000

for i in numbers:
    if i >= largest:
        largest = i
    if i <= smallest:
        smallest = i

print(f'{numbers}\n\nLargest number in list is {largest} and smallest number is {smallest}')
'''