#fin = open('words.txt')
#line = fin.readline()
#print(line)

#fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    print(word)

#Exercise 1 - Finding longwords.
def longwords(numchar):
    fin = open ('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > numchar:
            print(word, len(word))

#print(longwords(20))

def has_no_e(word):
    word = word.strip()
    for letter in word:
        if letter == "e": 
            return False
    return True

#print(has_no_e('hello'))
#print(has_no_e('Babson'))
#print(has_no_e('Everest'))

#ALTERNATE: 
def has_no_e_simple(word):
    return not 'e' in word

#print(has_no_e_simple("ea sports"))

def find_words_no_e():
    fin = open('words.txt')
    noecount = 0
    totalcount = 0
    for line in fin:
        totalcount += 1
        word = line.strip()
        if has_no_e(word):
            noecount += 1
            #print(word)
    noeratio = noecount / totalcount
    noeratio = noeratio * 100
    return noeratio

print("The percentage of the words with no 'e' is {:.2f}%.".format(find_words_no_e()))

def avoids(word,forbidden):
    word = word.strip()
    for letter in word:
        if letter in forbidden: 
            return False
    return True

print(avoids('Babson','ab'))
print(avoids('College','ab'))

def find_words_no_vowels():
    fin = open('words.txt')
