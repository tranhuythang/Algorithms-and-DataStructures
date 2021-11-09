# List: append, extend(list), insert(index, elem)
list1 = []
list2 = [1, 2, 'hello', 3.15]
list3 = ['a', 3]
print(list1)
print(list2)
list2.extend(list3)
list2.insert(3, "number 3")
print(list2)
del(list2[5])
print(list2)
list1.clear()
print(list1)

list2.remove(3)
print(list2)
list2.pop() #pop the last element
print(list2)

# Dictionary
dict = {1:"a", 2:"b", "third":"c"}
print(dict)
dict[3] = "d"
dict["third"] = "c1"
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())

print(dict.pop(2))
print(dict)

#Tuple
my_tuple = (1, 2, 3, 'edureka')
print(my_tuple[3][4])
for x in my_tuple:
    print(x)

tuple1 = (1, ) # one element tuple need to have comma
print(tuple1)

# Set
myset = {1, 2, 2, 3, 'four', 'four'}
print(myset)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)

print(set3)
print(set4)
print(set5)
print(set6)

# Stack and Queue:
# from collections import dequeue
# on the right: append(), pop()
# on the left: appendleft(), popleft()

from collections import deque
mystack = deque()
mystack.append(1)
mystack.append(2)
mystack.append(3)
mystack.appendleft(6)
mystack.appendleft(5)
print(mystack)



big = float("inf")
small = float("-inf")
print(big > 3)
print(small < -2)


