class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def recurse(openN, closedN):
            if (openN == closedN == n):
                res.append("".join(stack))
                return
            
            if (openN < n):
                stack.append("(")
                recurse(openN + 1, closedN)
                stack.pop()
            
            if (closedN < openN):
                stack.append(")")
                recurse(openN, closedN + 1)
                stack.pop()
        
        recurse(0, 0)
        return res