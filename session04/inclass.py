13 % 5
#Here we get the remainder of the division. In this case 3. 

13 // 2 
#If we use the double slash, we get whatever whole number. (NOT THE REMAINDER)

#UNIX EXAMPLE TIME

import time 
print (time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current // 60)//60 % 24
days = current // 60 // 60 // 24
print ('Current time: %d days, %d hours and %d minutes and %d seconds fom Epoch.' % (days, hours, minutes, second))
#THIS IS THE PROFESSORS ANSWER! COPIED IT FROM THE PRESENTATION! 

type(32)
#Using function type gives us the type of the argument. This case its an "int" as in intiger 

type(23.2)
#Type here is float

type('Hello')
#Type here is a string

type(hello)
#This is also a string. 

int(42)
#makes 42 an intiger

int(Hello)
#Returns an error

int(3.99)
#Here we only get the intiger part. Result: 3. It doesn't round. 

int(-2.4)
#here we get only the -2. 

#we can convert a string to a float number like this. 
float("3.14")

#absolute value
abs(-100)

abs(-110, 2)
#This returns an error. 

round(3.44)
round(3.49)
round(3.50)
round(-3.5)
round(3.65645485654,3)
#Rounds according to standards. 
#Can also specify how many decimal places we want!

min(2, 4, 6)
min(-2, 4, 10000)
#returns minimum value for that list. 

ord('$')
#Returns unicode id for that symbol

chr(36)
#Returns symbol for that unicode

isinstance(100.0,int)
#This can be used to make sure that the user has entered the correct type of information. 

import math

ratio = 100
math.log10(ratio)

degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)

#Exercise2 
#Try 2 math functions. Exponennt and raising to the power of: 

math.exp(3)
math.pow(2,3)



