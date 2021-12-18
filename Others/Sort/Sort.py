def bubbleSort(a):
    for k in range(len(a), 0, -1):
        print(k)
        for i in range(k - 1):
            if a[i] > a[i+1]:
                print('swap', a[i], a[i+1])
                a[i], a[i+1] = a[i+1], a[i]
    return a

def bubbleSortVerRecur(a, n=0):
    l = len(a) - n
    if l > 1:
        for i in range(l - 1):
            if a[i] > a[i+1]:
                print('swap', a[i], a[i+1])
                a[i], a[i+1] = a[i+1], a[i]
        bubbleSortVerRecur(a, n+1)

# print(bubbleSort([4, 6, 3, 1, 2, 7, 8]))
a = [9, 8, 7, 6, -1, -2, 3, 2, 1, 0]
bubbleSortVerRecur(a)
print(a)

