from multiprocessing.connection import wait
import os, time

from cv2 import waitKey

def točno_vrijeme():
    from datetime import datetime as dt
    
    vrijeme = dt.now()
    sati = vrijeme.hour
    minute = vrijeme.minute
    sekunde = vrijeme.second
    
    print(f'\n{sati} h {minute} min {sekunde} s\n')
    

    
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    točno_vrijeme()

    time.sleep(1)

    if not input():
        break
    
    