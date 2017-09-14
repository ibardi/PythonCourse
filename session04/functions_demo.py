
def print_lyrics():
    print("Hey Jude. Don't make it bad")
    print("Take a sad song and make it better.")

type(print_lyrics)
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print("NA - Na - Na - NA - NA, NA - NA - NA - NA")
    print_lyrics()

repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice("Steve")

my_name = "Jeff"
print_twice(my_name)

#My_abs function. Tested and it works correctly

def my_abs(numberentered):
    numoutput = abs(numberentered)
    print(numoutput)

my_abs(-15)
my_abs(2)
my_abs(-14)

#Variables and parameters are local example

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

# print(cat) - RREMOVED IT AS A COMMENT TO AVOID ERROR. 

#cat then returns a error claiming that "cat" is not defined. As cat is nested within the function. 

#Return values


def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')

print(give_me_a_break())

#Here the function does not print "another break". This is because the "return" terminates the function.

result = print_twice('Bing')
print(result)

def my_absmodified(numberentered):
    numoutput = abs(numberentered)
    return numoutput

print(my_absmodified(-120))

#Couldn't make the input() section work so I just added a random intiger for demonstration purposes. 

def nop():
    pass

#age = int(input())
age = 21
if age >= 18:
    pass

#Without pass, I am getting an error. 


def my_absmodz(numenter):
    output1 = abs(numenter)
    return output1

inputentered = input("Please enter a number to get its absolute value")
if isinstance(inputentered, int) or isinstance(inputentered, float):
    validenter = inputentered
    print(myabsmodz(validenter))
else:
    print('Please enter a valid integer or float')

#I am unable to test the whole function in the debugger because its not letting me enter an input. Otherwise should work. I tested its elements. 

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move (100, 100, 60, math.pi / 6)
print(x,y)

#This won't work because X is not defined. Obviously. 

