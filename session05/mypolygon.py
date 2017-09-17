import turtle
import math

tom = turtle.Turtle ()
print(tom)
#for i in range(4):
#    tom.fd(100)
#    tom.lt(90)

#for i in range(4):
#    print("hello!")

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(tom,200)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(tom,80,8)

def circle (t,r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t,length,n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int (arc_length / 3 ) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

#arc(tom,angle=270,r=80)
#This also demonstrate keyword arguments. 

def polyline(t, n, length, angle):
    """
    Draws n line segments with the given length and
    andgle (in degrees) between them. t is a turtle. 
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t,n,length):
    angle = 360.0 / n
    polyline(t,n,length, angle)

#polygon(tom, 4, 100)

turtle.mainloop()