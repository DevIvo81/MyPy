import collections, os

os.system('cls' if os.name =='nt' else 'clear')

red = collections.deque([1, 2, 3])

print(f'\nPočetni red - {red}\n')

red.append(4)
red.appendleft(5)


print(f'\nNovi red - {red}\n')

print(red.pop())
print()
print(red.popleft())
print()

print(f'\nPopanired - {red}\n')


