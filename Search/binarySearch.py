def binarySearch(a, x):
    left = 0
    right = len(a) - 1
    print("initial right", right)
    mid = (left + right) //2
    print("initial mid", mid)
    while left <= right:
        mid = ((left + right) // 2)
        print("calculated mid = ", mid)
        if x < a[mid]:
            print("left", left)
            right = mid + 1
        elif x > a[mid]:
            print("right", right)
            left = mid - 1
        else:
            print("found at", mid)
            return mid
    return -1

a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(binarySearch(a, 4))
print(binarySearch(a, 11))