
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

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
print("in_order_DFS")
solution = Solution()
solution.inorderDFS(n1)
solution.preorderDFS(n1)
solution.postorderDFS(n1)
solution.BFS(n1)
