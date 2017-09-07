15
#Scientific Notation
print(3.14e-2)

#Integer Addition (regular addition)
print(123+222)

#Floating - point multiplication
print(1.5*4)

#Raising to a power of some number
print(2**100)

#How many digits in a really BIG number. It takes a while for Python to run this. 
print(len(str(2**1000000)))

#Firs we import the math module and then we can use the tools within that module. 
import math
print(math.pi)
print(math.sqrt(85))

#Lets try Library Random
import random
print(random.random())
random.choice([1,2,3,4])
#Within random.choice, you put a collection of data, for the randomizer to cough up. 

# These: " [] " create a list. 


print('I\'m \"ok\".')

print('I\m leraning \nPython.')

print('\\\n\\')

print("\\\t\\")

print(r'\\\t\\')

print('''line 1
... line 2
... line 3 ''')

#BOOLEAN OPERATORS
print(3>5)
#This will yield false
#We want to use this for if statments, or conditionals, or loops. 

#logical operators: AND, OR, NOT
#True is case sensitive

print (True and True)
#TRUE

print (True and False)
#FALSE

print (False and False)
#FALSE

print(5>3 and 3>1)
#TRUE

print(True or True)
#TRUE

print(True or False)
#TRUE

print(False or False)
#FALSE

print(not True)
#FALSE

print(not False)
#TRUE

print(not 1>2)
#FALSE

agenum = int(input("Please enter your age:"))

if agenum > 21: 
    print('Yes, you can.')
else:
    print('Sorry.')