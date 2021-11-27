edges = [[1, 2], [2, 3], [3, 6], [6, 1], [4, 5], [5, 6], [6, 4]]

edges = [['a', 'b'], ['a', 'c'], ['a', 'f'], ['b', 'e'], ['c', 'd'], ['d', 'a'], ['d', 'h'], ['f', 'g'], ['e', 'f'], ['e', 'g'], ['e', 'h'], ['h', 'g']]
adj_list = {}
for s in edges:
    if s[0] not in adj_list:
        adj_list[s[0]]= set()
    if s[1] not in adj_list:
        adj_list[s[1]]= set()

for s in edges:
    adj_list[s[0]].add(s[1])
    # adj_list[s[1]].add(s[0])
# print(adj_list)

adj_list = {'a':['b', 'c', 'f'], 'b':['e'], 'e':['f', 'g', 'h'], 'f':['b', 'g'], 'd':['a', 'h'], 'h':['g'], 'g':[], 'c':['d']}
print(adj_list)

visited = []
pre = {}
post = {}
clock = 1

def DFS(root):
    if root is None:
        return
    global clock, pre, post, visited, adj_list

    pre[root] = clock
    clock = clock + 1
    visited.append(root)

    for child in adj_list[root]:
        if child not in visited:
            DFS(child)

    post[root] = clock
    clock = clock + 1

DFS('a')
print(visited)
for s in pre:
    print(s, pre[s], post[s])

