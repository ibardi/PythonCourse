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
    x = 3/4
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
            break
        x = y


#print("According to Python math, the square root is:", math.sqrt(par))

#Couldn't figure out how to print a proper table, so I did it manually. 

print(1.0,mysqrt(1.0),math.sqrt(1.0),abs(mysqrt(1.0)-math.sqrt(1.0)))
print(2.0,mysqrt(2.0),math.sqrt(2.0),abs(mysqrt(2.0)-math.sqrt(2.0)))
print(3.0,mysqrt(3.0),math.sqrt(3.0),abs(mysqrt(3.0)-math.sqrt(3.0)))
print(4.0,mysqrt(4.0),math.sqrt(4.0),abs(mysqrt(4.0)-math.sqrt(4.0)))
print(5.0,mysqrt(5.0),math.sqrt(5.0),abs(mysqrt(5.0)-math.sqrt(5.0)))
print(6.0,mysqrt(6.0),math.sqrt(6.0),abs(mysqrt(6.0)-math.sqrt(6.0)))
print(7.0,mysqrt(7.0),math.sqrt(7.0),abs(mysqrt(7.0)-math.sqrt(7.0)))
print(8.0,mysqrt(8.0),math.sqrt(8.0),abs(mysqrt(8.0)-math.sqrt(8.0)))
print(9.0,mysqrt(9.0),math.sqrt(9.0),abs(mysqrt(9.0)-math.sqrt(9.0)))
print(10.0,mysqrt(10.0),math.sqrt(10.0),abs(mysqrt(1.0)-math.sqrt(10.0)))