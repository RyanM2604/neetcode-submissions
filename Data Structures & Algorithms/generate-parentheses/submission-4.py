class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(sol, lparen, rparen):
            if lparen == rparen == n:
                res.append("".join(sol[:]))
                return
            
            if lparen > n:
                return
            
            if rparen > n:
                return
            
            if rparen > lparen:
                return
            
            sol.append('(')
            backtrack(sol, lparen + 1, rparen)
            sol.pop()

            sol.append(')')
            backtrack(sol, lparen, rparen + 1)
            sol.pop()
        

        backtrack([], 0, 0)
        return res