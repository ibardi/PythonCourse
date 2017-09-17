import turtle
import math

tom = turtle.Turtle ()
print(tom)
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def invpolygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.rt(360/n)

def circle (t,r):
    circumference = 2 * math.pi * r
    n = 150
    length = circumference / n
    polygon(t,length,n)

def invcircle (t,r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    invpolygon(t,length,n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int (arc_length / 3 ) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def invarc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int (arc_length / 3 ) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.rt(step_angle)


def leaf(t,r,angle):
    """
    This will draw one leaf. 
    """
    #since we repeat twice use a range of 2:
    for i in range (2):
        arc(t,r,angle)
        t.lt(180-angle)

def flowerhead (t,r,n,angle):
    """
    This draws the flower with n amount of leafs
    """
    for i in range (n):
        leaf(t,r,angle)
        t.lt(360.0/n)

#This function will draw the flowerhead.
radius = 100
numleafs = 6
anglechosen = 60

flowerhead(tom, radius, numleafs, anglechosen)

#Now the circle around it. We will stop drawing
tom.pu()

#Move to the outer edge of the circle
tom.fd(radius)

#Turn perpendicular
tom.lt(90)

#Start Drawing
tom.pd()

#Run the circle function
circle(tom,radius)

turtle.mainloop()