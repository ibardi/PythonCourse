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