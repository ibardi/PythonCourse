import random
import copy
import turtle
tom = turtle.Turtle()
tom.speed(1)
#ATTENTION: turtle's speed is set to slow for demonstration purposes! If running larger number of iterations, its best to set this at or near 10. 

def drunkard_walk(x, y, n):
    """
    x, y: the starting location
    n: the number of intersections(steps)
    This function uses the .random library to chose a random direction (north, east, south, or west) and then moves the turtle accordingly. Also the core functionality of the drunkward_walk.py is maintained within this program (Thereby, it has more code than is neccesary to just a turtle)
    """
    print(tom)
    overalldistance = 0
    originx = copy.deepcopy(x)
    originy = copy.deepcopy(y)
    for element in range(1,n+1):
        movetype = random.choice([1,2,3,4])
        if movetype == 1:
            tom.setheading(90)
            tom.fd(50)
            y += 1
            #print("North")
            #print(x,y)
        elif movetype == 2:
            tom.setheading(0)
            tom.fd(50)
            x += 1
            #print("East")
            #print(x,y)
        elif movetype == 3:
            tom.setheading(270)
            tom.fd(50)
            y += -1
            #print("South")
            #print(x,y)
        else:
            tom.setheading(180)
            tom.fd(50)
            x += -1
            #print("West")
            #print(x,y)
    horizontaldistance = abs(x - originx)
    verticaldistance = abs(y - originy)
    overalldistance = horizontaldistance + verticaldistance
    print("The drunkard started from (%d,%d)." % (originx, originy))
    print("The drunkard finished at (%d,%d)." % (x, y))
    print("After", n, "intersections, he's",overalldistance, "blocks from where he started.")
    turtle.mainloop()
    return overalldistance

#Testing
drunkard_walk(0,0,20)


#ATTENTION: The assignment asked for a function that calculates distance, which my function does. However, the assignment files also included print commands for certain elements which I intergrated within the function. it should be noted that these print commands are NOT neccesary and could be removed to simply the code.