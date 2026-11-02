# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            rightSide = None

            for i in range(qLen): # Always ends up with the right node since it goes left to right on the level of the tree
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSide:
                res.append(rightSide.val)
        
        return res