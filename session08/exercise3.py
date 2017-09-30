a = 'New String'

#Returns the position of the sub-script
print(a.find('w'))

#Case-Sensitive
print(a.find('s'))

#Returns '-1' for value if substring isn't within the string

print(a.find('f'))

#Start and Ends (here it doesn't find the 'w')
print(a.find('w',1,2))

#If we include the reference as 1 - 3, it will find it at the same position as first example.
print(a.find('w',1,3))

#We can also find largest substrings
print(a.find('Str'))
#It will return the STARTING point of the string (not all the values for each character).

print(a.find('Str',1,6))
#If the whole string is not present --> returns '-1'


#DISCLOSURE: I used this video for reference: https://www.youtube.com/watch?v=EGEt9e5TNq8
#It explains how the .find() function works. I used different parameters and extra steps to demonstrate my understanding AND that I am not just copying. 