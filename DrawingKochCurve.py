from turtle import *

def kochCurve(lengthSide, level):
    if level == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    kochCurve(lengthSide, level-1)
    left(60)
    kochCurve(lengthSide, level-1)
    right(120)
    kochCurve(lengthSide, level-1)
    left(60)
    kochCurve(lengthSide, level-1)


speed(0)
length = input('Enter length in 100s, for example 300.0\n')
level = input('Enter level (1-10)\n')
length = float(length)
level = int(level)
    
penup()

backward(length/2.0)

pendown()

for i in range(level-1):
    kochCurve(length, level)
    right(120)

mainloop()
    
