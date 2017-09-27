"""

a = 4
x = 3
epsilon = 0.0000001

y = (x + a/x) / 2
print(y)

x = y
y = (x +a/x) / 2
print(y)


x = y
y = (x +a/x) / 2
print(y)


x = y
y = (x +a/x) / 2
print(y)


x = y
y = (x +a/x) / 2
print(y)


x = y
y = (x +a/x) / 2
print(y)


x = y
y = (x +a/x) / 2
print(y)

while True:
    print(x)
    y = (x +a/x) / 2
    if abs(y-x) < epsilon:
        break
    x = y
"""
#Exercise 3
import math

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
            break
        x = y


#print("According to Python math, the square root is:", math.sqrt(par))


def test_square_root(n):
    """
    This function run the function: mysqrt(a) for a range provided by the n-value provided. For example, if n = 4, then the function will
    run mysqrt(1),mysqrt(2),mysqrt(3),and mysqrt(4). Even whole numbers have been converted to floats with a forced decimal value of 16, to ensure readability.
    """
    for n in range(1,n+1):
        print(n,"  ",'%.16f' % mysqrt(n),"  ",'%.16f' %math.sqrt(n),"  ",abs(mysqrt(n)-math.sqrt(n)))

test_square_root(9)


"""
THIS WAS THE ORIGINAL WAY THAT I DID IT. OBVIOUSLY THIS IS NOT TOO EFFICIENT. I CREATED A FOR LOOP
AS SEEN ABOVE, THAT SIMPLIFIES THE PROCESS AND ALLOWS FOR THE USER CHOOSE TOP A VALUE. 

print(1.0,mysqrt(1.0),math.sqrt(1.0),abs(mysqrt(1.0)-math.sqrt(1.0)))
print(2.0,mysqrt(2.0),math.sqrt(2.0),abs(mysqrt(2.0)-math.sqrt(2.0)))
print(3.0,mysqrt(3.0),math.sqrt(3.0),abs(mysqrt(3.0)-math.sqrt(3.0)))
print(4.0,mysqrt(4.0),math.sqrt(4.0),abs(mysqrt(4.0)-math.sqrt(4.0)))
print(5.0,mysqrt(5.0),math.sqrt(5.0),abs(mysqrt(5.0)-math.sqrt(5.0)))
print(6.0,mysqrt(6.0),math.sqrt(6.0),abs(mysqrt(6.0)-math.sqrt(6.0)))
print(7.0,mysqrt(7.0),math.sqrt(7.0),abs(mysqrt(7.0)-math.sqrt(7.0)))
print(8.0,mysqrt(8.0),math.sqrt(8.0),abs(mysqrt(8.0)-math.sqrt(8.0)))
print(9.0,mysqrt(9.0),math.sqrt(9.0),abs(mysqrt(9.0)-math.sqrt(9.0)))
"""