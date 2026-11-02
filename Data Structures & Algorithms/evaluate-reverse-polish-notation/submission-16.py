class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)

            elif token == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)

            elif token == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(float(b) / a))

            elif token == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)

            else:
                stack.append(int(token))
        
        return stack[-1]