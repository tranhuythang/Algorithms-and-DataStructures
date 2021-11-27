# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        def inorderDFS(node):
            if node == None:
                return
            else:
                inorderDFS(node.left)
                tree.append(node.val)
                inorderDFS(node.right)

        inorderDFS(root)
        return tree

Solution()
