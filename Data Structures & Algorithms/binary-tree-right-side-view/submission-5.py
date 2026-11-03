# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            q = collections.deque([root])
            res = []

            while q:
                qLen = len(q)
                level = []

                for i in range(qLen):
                    node = q.popleft()

                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                
                if level:
                    res.append(level.pop())
            
            return res
        
        return bfs(root)
    
