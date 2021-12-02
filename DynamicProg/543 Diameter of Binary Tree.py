"""
* Problem:
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
* Dynamic Programming on Tree algorithm:
Every diameter should go from the left-most node to right-most node of some node (not necessarily the root node). So for
each node, we find the height(node.left), height(node.right) and the diameter through that node becomes:
diameter = height(node.left) + height(node.right) + 2 if both height(node.left), height(node.right) >= 1
         = height(node.left) + 1 if node.right = None
         = height(node.right) + 1 if node.left = None
We find the diameter for each node and find the greatest diameter.

To calculate the height of a node, use Recursion and DFS
height(node) = max(height(node.left), height(node.right)) + 1 if node.left != None or node.right != None
             = 0 if node.left = None and node.right = None

* Time-Complexity: Each node is visited once so the time-complexity is O(n) where n is the number of nodes
* Space-Complexity: In the worst case where the tree is skewed, i.e. its edges are a line then the call-stack has n calls
i.e. the space-complexity in the worst case is O(n). When the tree is balanced, the space-complexity is O(log n)
"""
def DiameterBinaryTree(root):
    diameter = 0
    def dfs_dp(root):
        nonlocal diameter
        if root is None:
            return 0
        else:
            left_height = dfs_dp(root.left) + 1 if root.left else 0
            right_height = dfs_dp(root.right) + 1 if root.right else 0
            height = max(left_height, right_height)
            current_diameter = left_height + right_height
            if diameter < current_diameter:
                diameter = current_diameter
            return height
    dfs_dp(root)
    return diameter