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


radius = 100

#Turtle draws the main big circle
circle(tom,radius)

#Turtle reverses heading 180
tom.lt(180)

#Turtle draws the bottom half semi-circle
invarc(tom,(radius/2),180)

#Turtle draws the top half semi-circle
arc(tom,(radius/2),180)

#Resets the heading towards the south
tom.lt(90)

#Turns off the turtle drawing a line as it moves
tom.penup()

#Reposition the turtle
tom.fd(radius / 8 *3)

#Turns turtle to the west
tom.rt(90)

#Turns on the turtle drawing a line as it moves
tom.pendown()

#Draws the upper small circle
circle(tom,radius / 8)

#Turns of drawing
tom.penup()

#Turns to the south
tom.lt(90)

#Moves to next start position
tom.fd(((radius / 8) *5)+((radius/8) *3))

#Turn towards the east
tom.lt(90)

#Turns on drawing
tom.pendown()

#draws the bottom small circle
invcircle(tom,radius/8)

turtle.mainloop()