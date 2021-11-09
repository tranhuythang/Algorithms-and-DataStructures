import collections
a = [['a', 4, 5], ['b', 2, 3], ['c', 3, 3], ['d', 1, 1]]
# a.sort(key= lambda x:x[1], reverse= False)
b = sorted(a, key=lambda x:x[1], reverse=True)
print(a)
print(b)

x = [1, 5, 6, 2, 8, 8, 2, 5, 0]
try:
    print(x.index(5))
except:
    print("Not found")

x = "abc cdef "
print(x.find("c"))

x = ['c', 'b', 'A', 'C']
y = ['a', 'B', 'c']

x.sort(key= str.casefold)
print(x)

x = "522.4"
print("is number", x.isnumeric())

arr = [1, 1, 2, 3, 4, 1, 2, 5, 6, 7, 5, 8]
count = collections.Counter(arr)
print(count)
print(count[1], count[5])

for ind, val in enumerate(arr):
    print(ind, val)

print('a', 'b', 'c', end='x')
print('d')
print('e')

print('a', 'b', 'c', sep='x')

