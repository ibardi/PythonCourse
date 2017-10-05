#LISTS 

[10,20,30,40]
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

#Nested List
['spam', 2.0, 5, [10,20]]

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(AFC_east, numbers, empty)

#Mutable lists

AFC_east[3] = 'New York Giants'
print(AFC_east)

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print('Buffalo Bills' in AFC_east)
#This returns True or False

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]
#To get Apple


#To get Lisa 
print(L[-1][-1])

#To get "On Rail"

#Use of "for loop" and lists
for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] * 4
['Tom Brady', 'Bill Belichick']*3
#HERE It will yield a new list (NOT A STRING)

t = ['a', 'b', 'c', 'd', 'e', 'f']

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

#Exercise 2

t = ['a', 'b', 'c']
t.append('d')
print(t)
t.insert(2,'z')
print(t)
a = ['lol','whatsapp']
t.extend(a)
print(t)

#MAP, REDUCE, AND FILTER

#Mapping - Applying a funcition to each element within a lits
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#Reducing the list (bringing it togethre)
t = [1, 2, 3]
print(sum(t))

#Filter
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper("Babson College"))