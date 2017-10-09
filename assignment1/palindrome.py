def isPalindrome(s):
    """
    This function returns True if a word (or segment thereof of less than or equal to 2 in length) has the same first and last character. If the string is longer than 2 characters, then recursion occurs and the function checks the string without the previous first and last letters. This continues until either the function realizes a False or a True.
    """
    if len(s) <= 2 and s[-1] == s[0]:
        return True
    elif s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False

inputStr = input("Enter a string: ") 
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")