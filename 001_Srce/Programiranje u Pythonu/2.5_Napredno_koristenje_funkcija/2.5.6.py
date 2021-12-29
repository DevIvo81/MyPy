'''6.  Implementirajte generatorsku funkciju imena danUTjednu(), 
funkcija mora vratiti generator s danima u tjednu. Nakon što svi 
dani u tjednu budu otpušteni, ne kreće se ponovo s otpuštanjem 
vrijednosti od ponedjeljka. U glavnom programu pozivom 
implementirane generatorske funkcije ispišite sve dane u tjednu.'''
import os
os.system('cls')

def danUTjednu():
   tjedan = ['pon', 'uto', 'sri', 'cet', 'pet', 'sub', 'ned']
   for i in range(len(tjedan)):
       yield print(tjedan[i])

dan = danUTjednu()
next(dan)
next(dan)
next(dan)
next(dan)
next(dan)
next(dan)
next(dan)

