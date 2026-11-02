class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for bracket in s:
            if stack and bracket in lookup and lookup[bracket] == stack[-1]:
                stack.pop()
                continue
            
            stack.append(bracket)
        
        return stack == []