class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif token == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif token == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif token == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a / b))
            else:
                stack.append(token)
        
        return int(stack[-1])