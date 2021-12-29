import math, turtle
turtle.clear()
turtle.write("Lissajousova krivulja", move=False, align="center", font=("Tahoma", 30, "normal"))
## zadajemo parametre
a, b, delta = 3, 4, math.radians(0)
M = 350 # faktor uvećanja jer će ispis po radijanima biti presitan

## iscrtavamo krivulju
for t in range(360+1):
    phi = math.radians(t)   # preračunavamo stupnjeve u radijane, zbog uvjeta izračuna math trigonometrije
    x = M * math.sin(a*phi) # rezultat uvećavamo sa M radi jasnijeg ispisa
    y = M * math.sin(b*phi + delta)
    turtle.goto(x, y)
turtle.done()