#print(ord('a')-96)
#print(ord('z')-96)
#print(ord(' '))

#items =  ['bananas','rice','paprika','potato chips']
num1 = 'bananas'
num2 = 'rice'
num3 = 'paprika'
num4 = 'potato chips'

def priceofitem(a):
    price = 0
    for letter in a:
        if letter != " ":
            price = price + (ord(letter)-96)
        else:
            price = price
    return price

#little seperation
print("")
print("")
print("THIS IS PART ONE")
print("")
print("")

print(num1 + " " + "$"+str(priceofitem(num1)))
print(num2 + " " + "$"+str(priceofitem(num2)))
print(num3 + " " + "$"+str(priceofitem(num3)))
print(num4 + " " + "$"+str(priceofitem(num4)))
print("----------------------")
print("Total" + " " + "$"+str(priceofitem(num1)+priceofitem(num2)+priceofitem(num3)+priceofitem(num4)))


#little seperation
print("")
print("")
print("THIS IS PART TWO")
print("")
print("")

#Part 2
print('{:12}'.format(num1) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num1))))
print('{:12}'.format(num2) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num2))))
print('{:12}'.format(num3) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num3))))
print('{:12}'.format(num4) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num4))))
print("----------------------")
print('{:12}'.format("Total") + "   " + "$"+'{:4.2f}'.format(float(priceofitem(num1)+priceofitem(num2)+priceofitem(num3)+priceofitem(num4))))

#little seperation
print("")
print("")
print("THIS IS PART THREE")
print("")
print("")

#Part 3

#This is where i realized that I should've used a string for the above part!!!!
items =  ['bananas','rice','paprika','potato chips']
items2 =  ['bananas','rice','paprika']

def chklong(some_list):
    """
    This script finds the longest length word in a list. It returns the length of the longest word as an intiger. 
    """
    count = 0
    for i in some_list:
        if len(i) > count:
            count = len(i)
            word = i
    return int(len(word))

maximaxi = chklong(items2)
#I COULDN'T FIGURE OUT HOW TO FORMAT USING A VARIABLE INPUT ":maximaxi"??? I JUST MANUALLY ENTERED THE ":7" part.

print('{:7}'.format(num1) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num1))))
print('{:7}'.format(num2) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num2))))
print('{:7}'.format(num3) + "   " + "$"+ '{:4.2f}'.format(float(priceofitem(num3))))
print("-----------------")
print('{:7}'.format("Total") + "   " + "$"+'{:4.2f}'.format(float(priceofitem(num1)+priceofitem(num2)+priceofitem(num3))))

print("")
print("")