def GenerateParenthesis(n):
    p = [[] for i in range(n+1)]
    p[0].append("")
    p[1].append("()")
    temp = set()
    for i in range(1, n):
        temp = set()
        for str in p[i]:
            temp.add("()"+str)
            temp.add(str+"()")
            temp.add("("+str+")")
        for s in temp:
            p[i+1].append(s)
    return p[n]

test = [1, 2, 3, 4, 5, 6]
for n in test:
    print(n, '->', GenerateParenthesis(n))

test = [3, 0, -1, [], [1, 2], [], [1], []]
for n in test:
    if n:
        print('yes')
    else:
        print('no')

