#Exercise 1a
result = 0

for i in range (10):
    result = result + i + 1
    print("In the {}th iterations, new result = {}".format(i,result))

print (result)

#Exercise 1b
result = 0

for i in range (1000):
    result = result + i + 1
    print("In the {}th iterations, new result = {}".format(i,result))

print (result)

#Exercise 1 - Example of multiplication

result = 1

for i in range(1000):
    result = result * (i +1)
    print("in the {}th iteration, new result = {}".format(i,result))

print(result)

#Exercise 1c
result = 0

for i in range (1,1000,2):
    result = result + i + 1
    print("In the {}th iterations, new result = {}".format(i,result))

print (result)

#Exercise 1c part 2 (even)
result = 0

for i in range (0,1001,2):
    result = result + i + 1
    print("In the {}th iterations, new result = {}".format(i,result))

print (result)

#Character iterations
for c in 'hello':
    print(c)

#Word iterations
for alex in ['hello','world','babson','college']:
    print (alex)

import time
def countdown(n):
    while n > 0: 
        print(n)
        #time.sleep(1)
        n = n - 1
    print("Blastoff!")

countdown(10)

iteration = 0 
count = 0 

#Exercise2 - 1 - 1
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is:" + str(count))
    iteration += 1 
#1 = 12
#2 = 24
#3 = 36
#4 = 48
#5 = 60

#Exercise 2 - 1 - 2
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#1 = 12
#2 = 12
#3 = 12
#4 = 12
#5 = 12

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#0 = 1
#2 = 12
#3 = 1
#4 = 12
#5 = 1

#Break example 
"""
while True: 
    line = input("> ")
    if line == 'done':
        break
    print(line)

print('Done!')
"""
#This is usually used for a condiition to stop a loop. 

mysum = 0 
for i in range (5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)
#We get 5. 


mysum = 1
for i in range (5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)
#We get 22. Because -->  1 + 5 + 7 + 9 = 22