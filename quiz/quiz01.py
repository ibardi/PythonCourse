"""
Question 1:
"""


def crazy_about_9(a, b):
    """
    a, b: two integers
    Returns True if either one is 9, or if their sum or difference is 9. 
    """
    if a == 9 or b == 9:
        return True
    elif (a + b) == 9 or abs(a - b) == 9:
        return True
    else:
        return False
    

# When you've completed your function, uncomment the
# following lines and run this file to test!

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))


"""
-----------------------------------------------------------------------
Question 2:
A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
"""


def leap_year(year):
    """
    year(int): a year
    Returns True if year is a leap_year, False if year is not a leap_year.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False



# When you've completed your function, uncomment the
# following lines and run this file to test!
print("Question 2 check")
print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))


"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes The sum of all squares between
1 and n (inclusive).
"""

#THIS WAS MY ORIGINAL SUBMISSION, BUT I KNEW THAT IT DIDN'T WORK PROPERLY. I FIXED IT BETWEEN THE TIME OF ME PRESENTING IT AND SUBMITTING THE QUIZ. 
"""
def sum_squares(n):
    iteration = 1
    while iteration < n:
        print (iteration * iteration)
        iteration += 1
        if iteration > n:
            break


# When you've completed your function, uncomment the
# following lines and run this file to test!

print("Question 3 Check:")
print(sum_squares(1))
print(sum_squares(100))
"""

def sum_squaresfix(n):
    result = 0
    for i in range(1,n+1):
         result = result + (i*i)
    return result

print(sum_squaresfix(1))
print(sum_squaresfix(100))