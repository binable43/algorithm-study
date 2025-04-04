from collections import deque

class MyStack:

    def __init__(self):
        # Initilaize your data structure here
        self.__main_queue = deque()
        self.__sub_queue = deque()

    def push(self, x: int) -> None:
        # Push element x onto stack
        self.__main_queue.append(x)

    def pop(self) -> int:
        # Removes the element on top of the stack and returns that element
        ret = None
        while len(self.__main_queue) > 1:
            temp = self.__main_queue.popleft()
            self.__sub_queue.append(temp)

        if len(self.__main_queue) == 1:
            ret = self.__main_queue.popleft()
            self.__main_queue, self.__sub_queue = self.__sub_queue, self.__main_queue
        
        return ret

    def top(self) -> int:
        # Get the top element
        return self.__main_queue[-1]

    def empty(self) -> bool:
        # Returns whether the stack is empty
        return False if self.__main_queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()