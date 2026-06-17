class MyStack(object):

    def __init__(self):
        self.stack=[]        
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        x=self.stack.pop(-1)
        return x
    def top(self):
        return self.stack[-1]
    def empty(self):
        if self.stack==[]:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()