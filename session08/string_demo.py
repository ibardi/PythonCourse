team = 'New England Patriots'

# '-1' is the last character. 0 is the first character (we start from 0).

#print(team[-1])
#print(len(team))
#len() returns the amount of characters
#print(team[len(team)-1])
#We use square brakets because it refers to an INDEX (its a number in this case)
"""
for i in range(len(team)):
    if team[i] != " ":
        print(team[i])
"""

"""
#Another way to do it. 
for letter in team:
    if letter.isalpha():
        print(letter)

"""
"""
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    #if letter == "O" or letter =="Q": ---- OR WE CAN DO IT THIS WAY
    if letter in "OQ":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

"""

print(team[0:11])
print(team[12:20])

#OR

print(team[:11])
print(team[12:])

print(team[::-2])

#team[12:20] = "Seahawks"
#This print won't work because of the str issue. 
#print(team)

new_team = team[:12] + "Beavers"
print(new_team)

#Here we create a new variable. 

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team,"a"))

#looping and counting

word = "New England Patriots"
count = 0 
for letter in word:
    if letter == 'a': 
        count = count + 1
print(count)

#Exercise 2. 
def count(word, letter):
    c = 0 
    for x in word: 
        if x == letter:
            c = c + 1
    return c

print(count(team,'a'))

number_of_vowels = count(team,'a') + count(team,'e') + count(team,'i') + count(team,'o') + count(team,'u')
print(number_of_vowels)

#To make it more computer sciency

vowels = "aeiou"
number_of_vowels = 0 
for letter in vowels:
    number_of_vowels += count(team,letter)

print(number_of_vowels)

#To avoid distinguishing between upper and lower cases. 

def count(word, letter):
    lowerword = word.lower()
    c = 0 
    for x in lowerword: 
        if x == letter.lower():
            c = c + 1
    return c

print(count(team,'n'))

def in_both(word1,word2):
    for letter in word1:
        if letter in word:
            print(letter)


in_both("chicken","egg")