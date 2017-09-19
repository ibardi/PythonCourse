#I used this YouTube video for reference: https://www.youtube.com/watch?v=AJn843kplDw
"""
Basic concept: Take the larger number and divide it by the smaller number. Look for the remainder.
Then take the reminder and divide the divisor (smaller initial number) by the remainder. We continue this until the remainder = 0. 
The answer then is the last remainder. 
4220"""

intA = int(input("Enter first whole number: "))
intB = int(input("Enter second whole number: "))

def gcd(num1, num2):
    """
    This function relies on this part: num1 % num2.
     This part looks for the remainder. If there is a remainder, the
     function repeats itself, placing the remainder in the original spot of num1
     and the remainder of num1 % 2 as num2. If num2 is still not 0, it keeps going.
     Once num2 = 0, it returns num1 as the gcd. 
    """

    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1 % num2)

print(gcd(intA,intB))