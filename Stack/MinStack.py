class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.minStk or x <= self.minStk[-1]:
            self.minStk.append(x)

    def pop(self) -> None:
        x = self.stk.pop()
        if self.minStk and x == self.minStk[-1]:
            self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1] 

    def getMin(self) -> int:
        return self.minStk[-1]
        
