# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return False
            
            if sameSubTree(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        def sameSubTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return sameSubTree(p.left, q.left) and sameSubTree(p.right, q.right)
        
        return dfs(root)