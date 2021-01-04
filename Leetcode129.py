# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                res.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res