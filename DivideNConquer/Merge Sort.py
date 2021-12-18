def mergeSort(a):
    # def merge(a, b):
    #     if len(a) == 0:
    #         return b
    #     if len(b) == 0:
    #         return a
    #     if a[0] <= b[0]:
    #         return [a[0]] + merge(a[1::], b)
    #     else:
    #         return [b[0]] + merge(a, b[1::])

    def merge(a, b):
        alength = len(a)
        blength = len(b)
        i = 0
        j = 0
        result = []
        while i < alength and j < blength:
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        while i < alength:
            result.append(a[i])
            i += 1
        while j < blength:
            result.append(b[j])
            j += 1
        return result


    if len(a) <= 1:
        return a
    else:
        n = len(a)//2
        return merge(mergeSort(a[:n:]), mergeSort(a[n::]))

a = [1, 2, -2, -3, 5, 4, 0, 7]
a = [8, 9, -2, -3, 5, 4, 0, 6]
print(mergeSort(a))