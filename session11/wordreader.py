fin = open ('words.txt')


def dictdict():
    d = dict()
    for line in fin:
        d[line] = 1
    return d


#This has to be run to initialize

def checker(word):
    dictionary = dictdict()
    for key in dictionary:
        if dictionary[key] == word:
            return key
    raise LookupError()

print(checker('cat'))

#THIS IS NOT WORKING FOR SOME REASON. I SPENT A GOOD AMOUNT OF TIME TRYING TO FIGURE OUT WHY, BUT I WASN'T ABLE TO. 

#Part 2

testlist = [1,2,3,4,5,4]
testlist2 = [1,2,3,4,5]

def has_duplicates(x):
    dictionary = {}
    for element in x:
        dictionary[element] = 1 + dictionary.get(element, 0)
        if dictionary[element] > 1:
            return True
    return False

print(has_duplicates(testlist))
print(has_duplicates(testlist2))