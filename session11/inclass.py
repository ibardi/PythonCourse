print("")
print("Example of copying incorrectly")
t = [3,1,2]
t2 = t
print(t2)
t2.sort()
print("The sorted t2 list:",t2)
print("The 'unsorted' t list:",t)
print("")
#Since they are pointing to the same thing, both t2 and t will be sorted. 
print("Example of copying a list correctly")

p = [3,1,2]
#p2 = p.copy()
# or use this
p2 = p[:]

print("List p if printed:",p)
print("List p2 if printed:",p2)
print("")

#Examples of pop
s = [3,1,2]
s.pop()
print("Print of list s after pop():",s)
print("The pop() deletes the last element of the list and returns it.")
#We can also reference with a pop()
s.pop(0)
print("Printing of list s after pop() and pop(0):", s)
print("")

#Common Mistake with append
k = [1,2,3]
x = 4
k.append([x])
print(k)
print("In this scenario, we append x as a list within the list. We should avoid using [] within the append function")
print("The correct way to do it:")
m = [1,2,3]
y = 4
m.append(x)
print(m)
print("")