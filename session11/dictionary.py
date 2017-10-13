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

#Exercise 1
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

json_example = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "231",
               "short_name" : "231",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Forest Street",
               "short_name" : "Forest St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Babson Park",
               "short_name" : "Babson Park",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Wellesley",
               "short_name" : "Wellesley",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Norfolk County",
               "short_name" : "Norfolk County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Massachusetts",
               "short_name" : "MA",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "02457",
               "short_name" : "02457",
               "types" : [ "postal_code" ]
            },
            {
               "long_name" : "0310",
               "short_name" : "0310",
               "types" : [ "postal_code_suffix" ]
            }
         ],
         "formatted_address" : "231 Forest St, Babson Park, MA 02457, USA",
         "geometry" : {
            "location" : {
               "lat" : 42.2993708,
               "lng" : -71.2659951
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 42.3007197802915,
                  "lng" : -71.26464611970849
               },
               "southwest" : {
                  "lat" : 42.2980218197085,
                  "lng" : -71.26734408029149
               }
            }
         },
         "place_id" : "ChIJ7xQZi0GB44kRiWrnmTgf904",
         "types" : [ "establishment", "point_of_interest" ]
      }
   ],
   "status" : "OK"
}

print(json_example['results'][0]['address_components'][0]['long_name'])
print(json_example['results'][0]['address_components'][5]['long_name'])
print(json_example['results'][0]['address_components'][5]['short_name'])



def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('Value does not appear in the dictionary')

n = histogram('Massachusetts')
key = reverse_lookup(n,2)
print(key)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
 
hist = histogram('parrot')
print(hist)

inverse = invert_dict(hist)
print(inverse)

#Fibonacci Calculated
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)

#Exercise 3
"""
Global variables are variables that can be called on form outside of the function. Basically when you return x at the end of the function, that becomes global. While not returning the x, just printing it, would keep the variable x as local. We want to use global when we want to use the variable outside of just the one function. 
"""

