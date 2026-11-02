class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # Basically only required to keep track of if the min element gets popped as compared to minval

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
