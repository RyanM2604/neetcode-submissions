# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
            def dfs(root, maxSoFar):
                if not root:
                    return 0

                if root.val >= maxSoFar:
                    maxSoFar = root.val
                    return 1 + dfs(root.left, maxSoFar) + dfs(root.right, maxSoFar)
                else:
                    return dfs(root.left, maxSoFar) + dfs(root.right, maxSoFar)
            
            return dfs(root, -101)