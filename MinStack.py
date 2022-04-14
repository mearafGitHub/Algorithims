class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def pop(self) -> None:
        x = self.minstack[-1]
        self.minstack.remove(x)
        return x

    def push(self, val: int) -> None:
        self.minstack.append(val)
        self.minstack.sort()
        print(self.minstack)

    def getMin(self):
        return self.minstack[0]

    def top(self):
        return self.minstack[0]


one = MinStack()
print(one.push(1))
print(one.push(5))
print(one.push(2))
print(one.push(4))
print(one.push(7))
print(one.push(6))
print(one.push(-1))
print(one.push(9))
print(one.push(0))
print(one.push(1))
print(one.pop())
print(one.getMin())
print(one.top())