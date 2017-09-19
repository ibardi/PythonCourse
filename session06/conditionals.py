#THIS PRACTICE IS ABOUT CONDITIONAL STATEMENTS

#Simple if statement
age = 20
if age >= 18:
    print('Your age is',age)
    print('adult')

#If and else statements
age = 3
if age >= 18:
    print("your age is", age)
    print ('adult')
else:
    print("Your age is", age)
    print("teenager")

#Else if statements
age = 3
print('Your age is:', age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#Nested condiitonals
x = 5
y = 10
print("The values specified are: X =", x, "and Y =", y)
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print("x is less than y")
    else:
        print('x is greater than y')

#Exercise 1 
#Problem 1: BMI Calculator (Metric system). Weight in kilograms and height in meters 

systemused = str(input("What system would you like to use: 'imperial' or 'metric'"))
if systemused == "imperial":
    weight = float(input("Enter your weight in pounds"))
    height = float(input("Enter your height in inches"))
    bmi = 703 * (weight / (height**2))
    roundbmi = round(bmi,2)
    

elif systemused == "metric":
    weight = float(input("Enter your weight in kilograms"))
    height = float(input("Enter your height in meters"))
    bmi = weight / (height**2)
    roundbmi = round(bmi,2)
else:
    print("You entered an incorrect system. Check your spelling and make sure you do not use quotation marks!")

if roundbmi <= 18.5:
    print("Underweight")
elif roundbmi < 25:
    print("Normal weight")
elif roundbmi < 30:
    print("Overweight")
else:
    print("Obese")

#Problem 2:Two variables VarA and VarB
varA = "Troll"
varB = 55

if isinstance(varA,str) or isinstance(varB,str) == True:
    print("String involvled")
else:
    if varA > varB:
        print("varA is larger than varB")
    elif varA == varB:
        print("varA and varB is equal")
    else:
        print("varA is smaller than varB")

#RECURSIONS

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def print_n(s,n):
    if n<= 0:
        return
    print(s)
    print_n(s, n-1)

print_n("Hello",3)

#This is an example of infinite recursion. BELOW. 
def recurse():
    recurse()

#ON PURPOSE I AM NOT RUNNING THIS CAUSE IT CAUSES ISSUES.