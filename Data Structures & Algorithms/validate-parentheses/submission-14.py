class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for bracket in s:
            if bracket in lookup:
                if stack and stack[-1] == lookup[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return stack == []