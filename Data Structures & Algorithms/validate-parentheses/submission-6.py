class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for c in s:
            if c in myDict:
                if stack and stack[-1] == myDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []