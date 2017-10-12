names = ['Julian','Zach','Alex']
scores = [95,75,85]

grades = dict()
print(grades)
#Notice the squigly brackets

#To add something
grades['Zach'] = 75
print(grades['Zach'])

#To add multiple items:
grades = {'Zach':75,'Alex':85,'Julian':95}
print(grades)

#To add extra items
grades['Xiang']=88

#here we added an extra element. 
print(grades)
print(len(grades))

#Here we get a key error (like object not found)
#grades['Zhi']

#We can use in to chcek whether something is in a dictionary
print('Zach' in grades)
print('Zhi' in grades)

#Dictionary as a collection of counters
#If we want to do this with list

letters = [0,0]
string = "ababbaabaca"
for letter in string:
    if letter == "a":
        letters[0] += 1
    elif letter == "b":
        letters[1] += 1

print(letters)
#But we would have to do this for every single letter in the alphabet. Pain!!! Instead, we can use dictionaries. 

def histogram(st):
    d = dict()
    for c in st.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
#We generate keys only on occurance instead of generating it with value = 0, this way we save memory.

print(histogram('Bookkeeper'))

h = histogram("Bookkeeper")
print(h)

number_of_e = h.get('e',0)
number_of_a = h.get('a',0)
print(number_of_e)
print(number_of_a)

def histogramupdate(st):
    j = dict()
    for element in st.lower():
        j[element] = j.get(element,0) + 1
    return j

print(histogramupdate('dahello'))

""" NOT WORKING
def print_hist():
    for element in j: 
        print(element, j[element])

print_hist()
"""

for k,v in h.items():
    print(k,v)

