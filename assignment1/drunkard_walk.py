import random
import copy

def drunkard_walk(x, y, n):
    """
    x, y: the starting location
    n: the number of intersections(steps)
    This function uses the .random library to chose a random direction (north, east, south, or west) and then updates the x,y coordinates. The function further utilizes the .copy library to copy (not reference) the original coordinates. Then it calculates how many units horizontally and vertically the drunkard has moved. This is then added together to get the total distance travelled. Lastly, the function returns this number. Please note: the print(direction) and print(updatedcoordinates) are commented out, but left in on purpose to show how the program may be tested and verified.
    """
    overalldistance = 0
    originx = copy.deepcopy(x)
    originy = copy.deepcopy(y)
    for element in range(1,n+1):
        movetype = random.choice([1,2,3,4])
        if movetype == 1:
            y += 1
            #print("North")
            #print(x,y)
        elif movetype == 2:
            x += 1
            #print("East")
            #print(x,y)
        elif movetype == 3:
            y += -1
            #print("South")
            #print(x,y)
        else:
            x += -1
            #print("West")
            #print(x,y)
    horizontaldistance = abs(x - originx)
    verticaldistance = abs(y - originy)
    overalldistance = horizontaldistance + verticaldistance
    print("The drunkard started from (%d,%d)." % (originx, originy))
    print("The drunkard finished at (%d,%d)." % (x, y))
    print("After", n, "intersections, he's",overalldistance, "blocks from where he started.")
    return overalldistance

#Testing
drunkard_walk(3,344,3)
drunkard_walk(12,25,12)
drunkard_walk(-40,-1,60)
drunkard_walk(12,42,200)

#ATTENTION: The assignment asked for a function that calculates distance, which my function does. However, the assignment files also included print commands for certain elements which I intergrated within the function. it should be noted that these print commands are NOT neccesary and could be removed to simply the code.