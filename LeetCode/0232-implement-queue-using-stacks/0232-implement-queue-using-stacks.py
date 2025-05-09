class MyQueue:

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, x: int) -> None:
        while self.list1:
            self.list2.append(self.list1.pop())
        self.list1.append(x)
        while self.list2:
            self.list1.append(self.list2.pop())

    def pop(self) -> int:
        return self.list1.pop()

    def peek(self) -> int:
        return self.list1[-1]

    def empty(self) -> bool:
        return not self.list1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
