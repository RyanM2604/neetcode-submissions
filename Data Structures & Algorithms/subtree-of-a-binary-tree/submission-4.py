# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameSubtree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if not (p.val == q.val):
                return False
            
            return isSameSubtree(p.left, q.left) and isSameSubtree(p.right, q.right)
        
        if not root:
            return False
        
        if root.val == subRoot.val and isSameSubtree(root, subRoot):
            return isSameSubtree(root, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
