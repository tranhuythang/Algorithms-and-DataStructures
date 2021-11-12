def Listsubset_indexSizeK(input, k):
    """
    Generate subset_indexs of size k from a given set

    Recursion: assign a value for the i th element and then assign the i+1 th element until reaching kth element - append this subset_index to the result
    :param input:
    :param k:
    :return:
    """

    L = len(input)
    result = []
    subset_index = [-1 for i in range(k+1)]
    subset = []

    def assign(i):
        """ assign a value for ith element """
        for j in range(subset_index[i-1] + 1, L - k + i):
            subset_index[i] = j
            if i == k:
                subset = []
                for t in subset_index[1::]:
                    subset.append(input[t])
                result.append(subset)
            else:
                assign(i+1)
    assign(1)
    return result

test = [[['a', 'b', 'x', 'y'], 2], [[1, 2, 3, 4], 3], [[1, 2, 3, 4, 5, 6, 7], 3], [[1, 2, 3, 4, 5, 6, 7], 5]]
result = []
for s in test:
    result = Listsubset_indexSizeK(s[0], s[1])
    print(s[0], s[1], "->", len(result), result)