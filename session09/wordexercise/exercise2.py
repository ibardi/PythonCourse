#Exercise 2 - Homework for October 4th
print("Exercise 2:")
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print("Part 1: Standard")
print(is_abecedarian("hello"))
print(is_abecedarian("abel"))

# WITH RECURSION! 
def is_abecedarianrecursion(word):
    previous = word[0]
    if len(word) <= 1:
        return True
    if previous > word[1]:
        return False
    return is_abecedarianrecursion(word[1:])

print("Part 2: Recursion")
print(is_abecedarianrecursion("hello"))
print(is_abecedarianrecursion("abel"))

# WITH WHILE LOOP
def is_abecedarianwhile(word):
    count = 0
    while count < len(word)-1:
        if word[count +1] < word[count]:
            return False
        count = count + 1 
    return True

print("Part 3: While Loop")
print(is_abecedarianwhile("hello"))
print(is_abecedarianwhile("abel"))
