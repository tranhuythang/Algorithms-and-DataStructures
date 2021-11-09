def partitionLabels(s):
    """
    :type s: str
    :rtype: List[int]
    """

    global_alphabet = set([])
    for c in s:
        global_alphabet.add(c)

    print('global_alphabet: ', global_alphabet)
    local_alphabet = set([])

    start = 0
    end = 0
    count = 0
    partition = []

    for i in range(len(s)):
        local_alphabet.add(s[i])
        if len(local_alphabet) == len(global_alphabet):
            partition.append([start, i - start + 1])
            print("found at ", i)
            start = i + 1
            local_alphabet.clear()
        elif i == len(s) - 1:
            partition[-1] = [partition[-1][0], len(s) - partition[-1][0]]

    result = []
    for p in partition:
        result.append(p[1])
    return result
s = 'ababcbacadefegdehijhklij'
print(partitionLabels(s))
s = 'abcdbaaccdeabcdeab'
print(partitionLabels(s))
s = 'abcdbaaccdeabcdeabcdef'
print(partitionLabels(s))
