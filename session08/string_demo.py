team = 'New England Patriots'

# '-1' is the last character. 0 is the first character (we start from 0).

print(team[-1])
print(len(team))
#len() returns the amount of characters
print(team[len(team)-1])
#We use square brakets because it refers to an INDEX (its a number in this case)
"""
for i in range(len(team)):
    if team[i] != " ":
        print(team[i])
"""
#Another way to do it. 
for letter in team:
    if letter.isalpha():
        print(letter)