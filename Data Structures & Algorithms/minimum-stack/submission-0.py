class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini or self.mini[-1]>val:
            self.mini.append(val)
        else:
            self.mini.append(self.mini[-1])

    def pop(self) -> None:
        top=self.stack.pop()
        self.mini.pop()
        return top
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]