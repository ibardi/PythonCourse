fin = open('words.txt')
 
def findtriplepair():
    for line in fin:
        word = line.strip()
        count = 0
        numpairs = 0
        while count < len(word) - 1:
            if word[count] == word[count + 1]:
                numpairs += 1
                if numpairs == 3:
                     print(word)
                count += 2
            else:
                numpairs = 0
                count += 1

print("The triple pairs within this words.txt file are:")
findtriplepair()