class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for c in tokens:
            if c == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif c == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif c == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            else:
                stack.append(int(c))
        
        return stack[-1]