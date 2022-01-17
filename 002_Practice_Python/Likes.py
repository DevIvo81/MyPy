import os
os.system('cls')

noNames = []
oneName = ["Peter"]
twoNames = ["Jacob", "Alex"]
threeNames = ["Max", "John", "Mark"]
fourNames = ["Alex", "Jacob", "Mark", "Max"]

def likes(names):
    
    if not names:
        return print("no one likes this")
    elif len(names) == 1:
        return print(f"{names[0]} likes this")
    elif len(names) == 2:
        return print(f"{names[0]} and {names[1]} like this")
    elif len(names) == 3:
        return print(f"{names[0]}, {names[1]} and {names[2]} like this")
    else:
        return print(f"{names[0]}, {names[1]} and {len(names) - 2} others like this")
    
