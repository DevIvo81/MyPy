import os
os.system('cls' if os.name == 'nt' else 'clear')

#region SINGLETON

class Singleton:
    __singleton = None
    
    def __init__(self):
        if Singleton.__singleton == None:
           Singleton.__singleton = self
        else:
            raise Exception('SINGLETON!') 
    
    @staticmethod
    def get_instance():
        if Singleton.__singleton == None:
            Singleton()
        return Singleton.__singleton

s1 = Singleton()
print(s1)

# s2 = Singleton()
# print(s2)

s3 = Singleton.get_instance()
print(s3)

s4 = Singleton.get_instance()
print(s4)

#endregion



