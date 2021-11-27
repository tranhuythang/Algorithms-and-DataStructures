from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderDFS(self, root):
        result = []
        def inorderDFS_recursion(root):
            if root is None:
                return
            else:
                inorderDFS_recursion(root.left)
                result.append(root.val)
                inorderDFS_recursion(root.right)
        inorderDFS_recursion(root)
        print(result)

    def preorderDFS(self, root):
        result = []
        def preorderDFS_recursion(root):
            if root is None:
                return
            else:
                result.append(root.val)
                preorderDFS_recursion(root.left)
                preorderDFS_recursion(root.right)

        preorderDFS_recursion(root)
        print(result)

    def postorderDFS(self, root):
        result = []
        def postorderDFS_recursion(root):
            if root is None:
                return
            else:
                postorderDFS_recursion(root.left)
                postorderDFS_recursion(root.right)
                result.append(root.val)
        postorderDFS_recursion(root)
        print(result)

    def BFS(self, root):
        visited = []
        found_queue = deque()
        found_queue.append(root)
        while len(found_queue) != 0:
            current_node = found_queue.popleft()
            visited.append(current_node.val)
            if current_node.left not in visited and current_node.left is not None:
                found_queue.append(current_node.left)
            if current_node.right not in visited and current_node.right is not None:
                found_queue.append(current_node.right)
        print(visited)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

solution = Solution()
# solution.inorderDFS(n1)
# solution.preorderDFS(n1)
# solution.postorderDFS(n1)
print('Solution_BFS')
solution.BFS(n1)

class NodeWithChildren:
    def __init__(self, val):
        self.val = val
        self.children = []

class GraphSearch:
    def BFS_node(self, root):
        nodes_to_explore = deque()
        visited_node = []
        nodes_to_explore.append(root)
        while nodes_to_explore:
            current_node = nodes_to_explore.popleft()
            visited_node.append(current_node)
            for child_node in current_node.children:
                if child_node not in nodes_to_explore:
                    nodes_to_explore.append(child_node)
        print(list(map(lambda x: x.val, visited_node)))

    def BFS_shortestpath(self, source, target):
        nodes_to_explore = deque()
        visited = []
        previous_node = {}
        nodes_to_explore.append(source)
        path = [target.val]
        distance = {}
        distance[source.val] = 0
        while nodes_to_explore:
            current_node = nodes_to_explore.popleft()
            visited.append(current_node)
            temp_node = None
            if current_node is target:
                temp_node = current_node
                while temp_node is not source:
                    temp_node = previous_node[temp_node]
                    path.append(temp_node.val)
                break
            for child_node in current_node.children:
                if child_node not in visited:
                    nodes_to_explore.append(child_node)
                    previous_node[child_node] = current_node
                    distance[child_node.val] = distance[current_node.val]+1
        return path[::-1], distance[target.val]


graph_search = GraphSearch()

# Graph 1
n1 = NodeWithChildren(1)
n2 = NodeWithChildren(2)
n3 = NodeWithChildren(3)
n4 = NodeWithChildren(4)
n5 = NodeWithChildren(5)
n1.children.append(n2)
n1.children.append(n3)
n2.children.append(n4)
n2.children.append(n5)

print('graph_search: BFS')
graph_search.BFS_node(n1)


# Graph 2
a = NodeWithChildren('A')
b = NodeWithChildren('B')
c = NodeWithChildren('C')
d = NodeWithChildren('D')
e = NodeWithChildren('E')
s = NodeWithChildren('S')

a.children = [b, s]
b.children = [a, c]
c.children = [b, s]
s.children = [a, c]
d.children = [e, s]
e.children = [s, d]

print('graph_search: BFS')
print("shortest path = ", graph_search.BFS_shortestpath(s, b))

# graph 3
a = NodeWithChildren('a')
b = NodeWithChildren('b')
c = NodeWithChildren('c')
d = NodeWithChildren('d')
e = NodeWithChildren('e')
f = NodeWithChildren('f')
g = NodeWithChildren('g')
h = NodeWithChildren('h')

a.children = [b, c]
b.children = [d, e]
c.children = [f, g]
e.children = [h]

print('graph_search: BFS')
print("shortest path = ", graph_search.BFS_shortestpath(a, h))