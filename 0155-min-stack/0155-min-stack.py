class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min:
            self.min.append(value)
        else:
            self.min.append(min(value, self.min[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]

    def getMin(self) -> int:
        if self.stack: return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()