class MinStack:
    def __int__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        self.stack.append(value)
        small = min(value, self.minstack[-1] if self.minstack else value)
        self.minstack.append(small)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def getmin(self):  # O(1)
        return self.minstack[-1]

    def top(self):
        return self.stack[-1]