prnt ('Hello, Word')
# The error: "NameError: name 'prnt' is not defined" is returned, as prnt is an undefined in terms of Python, as such the program does not understand what I am asking of it.

#1a Lack of  One Parenthesis
print ("Hello, World"
#ANSWER: Same as #1b, Python warns about the lack of the parentheses and returns a syntax error. 

#1b Lack of Both parenthesis
print "Hello, World"
#ANSWER: Returns "SyntaxError: Missing parentheses in call to 'print". Here python returns a syntax error where it explicitly points out the issues = missing the parentheses. 

#2a Lack of One quotation mark
print ("Hello, World)
#ANSWER: Returns "SyntaxError: EOL while scanning string literal". This is because the string is incomplete. The quotation mark at the end would designate the end of the string; however, python cannot find it, and so it doesn't have the ability to print the string. 

#2b Lack of both quotations marks 
print (Hello, World)
#ANSWER: Here Python tries to find "Hello" as a defined parameter. It doesn't recognize it as a string (text), but rather thinks of it as a predefined value which it should be supposed to be able to reference. 

#3 Adding + in front of a number? 
print (2++2)
#ANSWER: Python successfully prints "4" as a result. The logic being "2" and "positive 2" are is still equal to 4. 

#4 Leading Zeros?
print (02+40)
#ANSWER: Python returns a "SyntaxError: invalid token", as "02" should be represented as "2" and so it doesn't understand the token. 

#5 Two Values with No operators between
print (20 43)
#ANSWER: It returns a "SyntaxError: invalid Syntax". It won't work. 