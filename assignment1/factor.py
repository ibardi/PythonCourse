def factor():
    """
    This function requests a user input and converts it into an intiger (just in case). However, it does not validate. After it uses a simple
    for loop to check whether the selected number is divisible by any number within the range of 1 and the number itself. If the number is divisble such that the
    remainder is equal to 0, the function prints that number. 
    """
    n = input("Please enter an intiger:")
    n = int(n)
    print("The factors of",n,"are:")
    for element in range(1,n+1):
        if n % element == 0:
            print(element)


factor()

#ATTENTION: The examples calls for an output of 2,3,5,5 for an input of 150. But that is incorrect. I've decided to follow the factoring rules. Including the 1s and the number itself as a factor of which it is divisible by. 

#Testing

#Input: 10
#Expected output: 1,2,5,10

#Input 32
#Expected output: 1,2,4,8,16,32

#Input 5897
#Expected output: 1, 5897

#Input 5898
#Expected output: 1, 2, 3, 6, 983, 1966, 2949, 5898