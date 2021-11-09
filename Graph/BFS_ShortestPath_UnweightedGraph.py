from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def BFS_ShortestPath_UnweightedGraph_verNode(start, end):
    tobeexplored_queue = deque()
    tobeexplored_queue.append(start)
    distance = {}
    distance[start.val] = 0
    pre = {start.val : start.val}
    while len(tobeexplored_queue) != 0:
        current_node = tobeexplored_queue.popleft()

        for child in current_node.children:
            if child.val not in distance:
                tobeexplored_queue.append(child)
                distance[child.val] = distance[current_node.val] + 1
                pre[child.val] = current_node.val

    print(distance[end.val])
    path = []
    nodeval = end.val
    while nodeval != start.val:
        path.append(nodeval)
        nodeval = pre[nodeval]
    path.append(start.val)
    print(path[::-1])


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
s = Node('S')
a.children = [b, s]
b.children = [c, a]
c.children = [s, b]
s.children = [a, d, e, c]
d.children = [e, s]
e.children = [s, d]

BFS_ShortestPath_UnweightedGraph_verNode(b, e)

def BFS_ShortestPath_UnweightedGraph_verAdjList(vertex_count, edges, start, end):
    adj_list = {}
    for i in range(vertex_count):
        adj_list[i] = set()
    for s in edges:
        adj_list[s[0]].add(s[1])
        adj_list[s[1]].add(s[0])

    print("adjacency_list", adj_list)

    ToBeExploredQueue = deque()
    ToBeExploredQueue.append(start)
    distance = {start:0}
    pre = {start:start}
    while(len(ToBeExploredQueue) != 0):
        current_node = ToBeExploredQueue.pop()
        for child in adj_list[current_node]:
            if child not in distance:
                ToBeExploredQueue.append(child)
                distance[child] = distance[current_node] + 1
                pre[child] = current_node
    print(distance[end])
    path = []
    node = end
    while node != start:
        path.append(node)
        node = pre[node]

    path.append(start)
    print(path[::-1])

BFS_ShortestPath_UnweightedGraph_verAdjList(7, [[1, 2], [2, 3], [3, 6], [6, 1], [4, 5], [5, 6], [6, 4]], 2, 5)







