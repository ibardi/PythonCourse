#1 How Many Seconds are there in 42 minutes and 42 seconds
print (42+42*60)
# We are able to use the order of operatoins to our advantage. To demonstrate, I put the extra 42 seconds in the begining. However, Python will first multiply the 42 by 60 and then add 42 (which is the correct order with regards to math). 
#It also works the other way around
print (42*60+42)
#This prints the same answer: 2562 seconds

#2 How many miles are there in 10 kilometers
print (10/1.61)
#There are 6.211 miles in 10 km

#3 If you run a 10 kilometer race in 42 minutes and 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is you average speed in miles per hour? 
print ((42*60+42)/(10/1.61))
#The above line, yields the answer of "412.482" seconds per mile. OR
print ((42*60+42)/(10/1.61)/60)
#Expressed in minutes (divided by 60) it yields "6.87" minutes / mile. 

#Miles / hour
print((1*60*60)/((42*60+42)/(10/1.61)))
#The average speed is 8.73 miles / hour. To get this we devide the number of seconds in an hour (1*60*60) by the seconds taken to travel 1 mile.


#     THIS POINT ON IS EXERCISE 1 FROM SESSION 2 -----

#QUESTION 1 Volume of a Sphere (assuming pi as 3.14)
r = 5
v = (4/3)*3.14*r**3
print('The volume of the sphere is', v)
#ANSWER Volume of the sphere is 523.333333333 continuing. 

#Question 2 - Book Calculation
copies = 60
coverprice = 24.95
discount = 0.4
shipping = 3 + (0.75*(copies-1))
cost = (coverprice * (1-discount)* copies) + (shipping)
print('The wholesale cost of 60 copies is $%.2f' % cost)
#ANSWER $945.45 is the wholesale cost for 60 copies

#Question 3 
starttime = 6 + (52/60)
num1legpace = 8+(15/60)
num1legdistance = 1
num1legtime = num1legdistance * num1legpace
num2legpace = 7 + (12/60)
num2legdistance = 3
num2legtime = num2legdistance * num2legpace
num3legtime = num1legtime
fulltime = num1legtime + num2legtime + num3legtime
fulltimeinhours = fulltime / 60
arrivaltime = starttime + fulltimeinhours
print(arrivaltime)
#The arrival time is approximately at 7:30AM!

#Question 4 - Average Grade Rise
percentagechange = (89-82) / 82 * 100
print('The percentage change is %.1f'% percentagechange,'%')
#ANSWER 8.5% Change