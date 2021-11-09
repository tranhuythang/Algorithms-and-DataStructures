def mergeSort(a):
    def merge(a,b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[0] <= b[0]:
            return [a[0]] + merge(a[1::], b)
        else:
            return [b[0]] + merge(a, b[1::])

    if len(a) <= 1:
        return a
    else:
        n = len(a)//2
        return merge(mergeSort(a[:n:]), mergeSort(a[n::]))

a = [1, 2, -2, -3, 5, 4, 0, 7]
a = [8, 9, -2, -3, 5, 4, 0, 6]
print(mergeSort(a))