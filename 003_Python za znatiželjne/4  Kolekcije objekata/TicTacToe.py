import os, string

os.system('cls')

print()

def polje():

    a = list("  7  |  8  |  9  ")
    print(*a)
    b = list("-----+-----+-----")
    print(*b)
    c =list("  4  |  5  |  6  ")
    print(*c)
    d = list("-----+-----+-----")
    print(*d)
    e = list("  1  |  2  |  3  ")
    print(*e)
    print()
    
          
    br1 = 0
    br2 = 0
    while br1 < 8 and br2 < 8: 
        p1 = int(input("Unesi broj polja na koje želiš staviti X: "))
        if p1 not in range(10) and p1.isdigit() == False:
            print("Krivi broj!")
        else:
            for i in range(17):
                if a[i] == p1:
                    a[i] == p1


polje()
