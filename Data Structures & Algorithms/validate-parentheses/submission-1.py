class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        bracketDict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for bracket in s:
            if bracket in bracketDict:
                if stack and stack[-1] == bracketDict[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return stack == []