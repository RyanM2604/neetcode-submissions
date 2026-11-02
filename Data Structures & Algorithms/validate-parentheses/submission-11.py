class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for bracket in s:
            if bracket in lookup and stack and stack[-1] == lookup[bracket]:
                stack.pop()
            else:
                stack.append(bracket)
        
        return stack == []