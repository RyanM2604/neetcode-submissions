class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []
        for c in s:
            if c in brackets and stack and stack[-1] == brackets[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return stack == []