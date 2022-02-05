import collections, os

os.system('cls' if os.name =='nt' else 'clear')

c = collections.Counter("abrakadabra")

print(c)

print(c["a"])

c += collections.Counter('ćiribu ćiriba')

print(c)

print(c.most_common(3))

