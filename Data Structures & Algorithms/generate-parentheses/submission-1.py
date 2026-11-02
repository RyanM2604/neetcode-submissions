class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open == closed == n, append to res
        # if open < n, append "(" to stack and recurse
        # if closed < open, append ")" to stack and recurse

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop() # must pop on unwind to reset global stack var
            
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res