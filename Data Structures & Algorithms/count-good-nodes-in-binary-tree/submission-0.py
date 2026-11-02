# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, greatest):
            nonlocal res
            if not root:
                return 

            if root.val >= greatest:
                res += 1
            
            greatest = max(root.val, greatest)

            dfs(root.left, greatest)
            dfs(root.right, greatest)

        dfs(root, -float('inf'))

        return res
