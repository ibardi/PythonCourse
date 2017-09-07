#1.1 Number value --> 5
a = 3 
print(a + 2)

#1.2 Error because A is not defined.
a = a + 1.0
print(a)

#1.3 Not Defined = Error
a = 3
print(b)

#1.4 BOOLEAN Value --> False
a = 3
a == 5.0
print(a)

#1.5 BOOLEAN Value --> True
b = 10
c = b > 9
print(c)

#1.6 BOOLEAN Value --> True
print(5/2 == 5/2.0)

#2.1 BOOLEAN Value --> False
print(3.0 - 1.0 != 5.0 - 3.0)

#2.2 BOOLEAN Value --> False
print (3 > 4 or (2<3 and 9 > 10))

#2.3 BOOLEAN Value --> True
print (4 > 5 or 3 < 4 and 9 > 8)

#2.4 BOOLEAN Value --> False
print(not(4>3 and 100 >6))

#3 Formatting Time
#I used this documentation to help me understand: https://www.tutorialspoint.com/python/python_date_time.htm
#used the assumption that there are 86,400 seconds in a day
import time
localtime = time.localtime(time.time())
hoursx = localtime[3]
minutesx = localtime[4]
secondsx = localtime[5]
currenttime = hoursx, minutesx, secondsx
print("The current time is: %s:%s:%s" %(hoursx,minutesx,secondsx))
ssepoch = time.time()
dayssepoch = ssepoch / (60*60*24)
print("Days passed since last epoch (rounded down to the nearest full number): %.0f" % (dayssepoch))