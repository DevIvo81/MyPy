import os

os.system('cls')

pojam = input("\n\nUnesi pojam: ")

print()
print()
 
 
print("\n\nPogodi slova\n\n")
 
pogoci = ''
 
# any number of brojpok can be used here
brojpok = 12
 
 
while brojpok > 0:
      
    krivo = 0
     
    for s in pojam:
         
        # comparing that sacter with
        # the sacter in pogoci
        if s in pogoci:
            print(s, end=" ")
             
        else:
            print("_", end=' ')
             
            # for every failure 1 will be
            # incremented in failure
            krivo += 1
             
 
    if krivo == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")
         
        # this print the correct pojam
        print("Pojam je: ", pojam)
        break
     
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    pokušaj = input("pokušaj a sacter:")
     
    # every input sacter will be stored in pogoci
    pogoci += pokušaj
     
    # check input with the sacter in pojam
    if pokušaj not in pojam:
         
        brojpok -= 1
         
        # if the sacter doesn’t match the pojam
        # then “Wrong” will be given as output
        print("Wrong")
         
        # this will print the number of
        # brojpok left for the user
        print("You have", + brojpok, 'more pogoci')
         
         
        if brojpok == 0:
            print("You Loose")