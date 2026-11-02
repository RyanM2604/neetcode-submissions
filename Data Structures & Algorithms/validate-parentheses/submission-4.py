class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for bracket in s:
            if bracket in myDict and stack and myDict[bracket] == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        
        return stack == []
        