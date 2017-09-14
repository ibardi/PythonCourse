valuea = 9
valueb = -12
valuec = 4

def quadratic(a, b, c):
    import math
    discr = b**2 - 4*a*c
    if discr >= 0:
        root1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
        root2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
        if root1 == root2:
            print("There is only one root, which is:", root1)
        else:
            print("Root 1 is:", root1," ", "Root 2 is:", root2)
    else:
        print("The roots are imaginery")

quadratic(valuea,valueb,valuec)