def ListPermutation(input):
    L = len(input)
    original_set = set(input)
    current_permutation = [None for i in range(L)]

    result = []
    def assign(i):
        print('assign for i = ', i)
        if i == 0:
            value = input[::]
        else:
            value = original_set.difference(set([current_permutation[j] for j in range(i)]))
        print('  value = ', value)
        for j in value:
            current_permutation[i] = j
            print('  pick j = ', j)
            if i<L-1:
                assign(i+1)
            else:
                result.append([current_permutation[k] for k in range(L)])
    assign(0)
    return result

test = [[1, 3, 5, 7], [1, 2, 3], [1, 2]]
for s in test:
    result = ListPermutation(s)
    print(s, '->', len(result), result)

