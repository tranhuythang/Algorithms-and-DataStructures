import collections

def test7():
    bigList = []
    l1 = [1, 2]
    bigList.append(l1)
    bigList.append(l1)
    print(bigList)     #[[1, 2], [1, 2]]
    l1[0] = 3
    print(bigList)     #[[3, 2], [3, 2]]

test7()

def test6():
    list1 = ["a", "b", "c"]
    list2 = ["a", "b", "c"]
    list3 = ["b", "c", "a"]
    print(list1 == list2)   #True
    print(list1 == list3)   #False
    print(collections.Counter(list1) == collections.Counter(list3))  #True

    list1 = [[1, 2], [3, 4], [5, 6]]
    list2 = [[3, 4], [5, 6], [1, 2]]
    my_sort = lambda x: 100*x[0] + x[1]
    print(sorted(list1, key=my_sort) == sorted(list2, key=my_sort))  # True

    set1 = set([1, 2, 3])
    set2 = set([3, 1, 2])
    print(set1 == set2)    #True

    dict1 = {'a': 1, 'b': 2, 'c':3}
    dict2 = {'b': 2, 'c': 3, 'a': 1}
    print(dict1==dict2)    #True

def test5():
    a = ["abc", "dce", "2ef"]
    b = ["dce", "2ef", "abc"]
    c = ["abc", "dce", "2ef"]
    print(a == b)
    print(a == c)

    a = {'a': 1, 'b': 2, 'c':3}
    b = {'b': 2, 'c': 3, 'a': 1}
    print(a==b)

    x = [[5, 6], [1, 2], [3, 4]]

    toStr = lambda x: str(x[0])+'||'+str(x[1])
    print(toStr(x))
    print(list(map(toStr, x)))
    # print(collections.Counter(a))

def test4():
    a = [['a', 4, 5], ['b', 2, 3], ['c', 3, 3], ['d', 1, 1]]
    # a.sort(key= lambda x:x[1], reverse= False)
    b = sorted(a, key=lambda x:x[1], reverse=True)
    print(a)
    print(b)

def test3():
    x = [1, 5, 6, 2, 8, 8, 2, 5, 0]
    try:
        print(x.index(5))
    except:
        print("Not found")

    x = "abc cdef "
    print(x.find("c"))

def test3():
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

def test1():
    print('a', 'b', 'c', end='x')
    print('d')
    print('e')

    print('a', 'b', 'c', sep='x')
