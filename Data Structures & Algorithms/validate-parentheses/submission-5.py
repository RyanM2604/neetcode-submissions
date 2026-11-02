class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for bracket in s:
            if bracket in myDict and stack and stack[-1] == myDict[bracket]:
                stack.pop()
            else:
                stack.append(bracket)
        
        return stack == []