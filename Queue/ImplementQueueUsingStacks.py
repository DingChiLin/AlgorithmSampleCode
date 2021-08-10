class MyQueue:
    def __init__(self):
        self.stk = []
        self.rStk = [] # reversed stack
        return None

    def push(self, x: int) -> None:
        self.stk.append(x)

    def _move(self): # move all the elements in stk to rStk and reverse their order
        while self.stk:
            n = self.stk.pop()
            self.rStk.append(n)

    def pop(self) -> int:
        if not self.rStk:
            self._move()
        return self.rStk.pop()

    def peek(self) -> int:
        if not self.rStk:
            self._move()
        return self.rStk[-1]

    def empty(self) -> bool:
        return not self.stk and not self.rStk