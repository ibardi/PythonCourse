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

radius = 120
def hourglass(t):
    """
    This function draws the hour glass with the two circles inside. It calculates the circles radius based on
    the parameters given for the trianglelength, which in turn is based on the defined radius.
    """
    triangleleg = radius
    standardturn = 360 / 3

#Turtle moves left to creat the BOTTOM part of the hourglass. 
    tom.fd(triangleleg)

#Turtle turns left
    tom.lt(standardturn)

#Turtle moves forwards to create another side of the triangle AND the left side of the top triangle.
    tom.fd(triangleleg / 2)

#I am using the formula radius = (2*a) / p, where a, is area of the triangle, and p is the perimeter of a triangle. 
# Since its an equilaterle triangle, I use the formula: Area = sqrt of 3, devided by 4 * length of side to the power of 2. 
    areatriangle = ((3**0.5)/4) * triangleleg**2
    incircleradius = (2 * areatriangle) / (triangleleg *3)
    circle(tom,incircleradius)

#Turtle continues on its original path
    tom.fd(triangleleg *1.5)

#Turtle turns to a parallel (facing east).
    tom.lt(360- (360 + (standardturn)))

#Turtle draws the top line
    tom.fd(triangleleg)

#Turtle turns towards the center of the circle
    tom.rt(standardturn)

#Turtle crosses the center of the circle to form last two missing lines of both triangles.
    tom.fd(triangleleg /2)

#Turtle does the other circle
    invcircle(tom,incircleradius)

#Turtle continues on its path
    tom.fd(triangleleg *1.5)
#Turtle points perpendicular
    tom.lt(90)
 

hourglass(tom)

circle(tom,radius)

#Now we line up so that we only have to run the hourglass function again. Its, easier for us to line up by using exisitng lines.

#Turns back on the long diagonal line
tom.lt(90)

#moves to the center
tom.fd(radius)

#Turns to the right. 
tom.rt(90)

#moves to position of start
tom.fd(radius)

#We set an appropriate heading start NORTH (90).
tom.setheading(90)

#We re-run the hourglass function. 
hourglass(tom)
turtle.mainloop()