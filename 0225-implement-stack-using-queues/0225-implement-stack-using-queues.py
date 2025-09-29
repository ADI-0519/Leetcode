from collections import deque
class MyStack:

    def __init__(self):
        
        self.stk = deque()

    def push(self, x: int) -> None:
        
        self.stk.append(x)

    def pop(self) -> int:
        
        item = self.stk.pop()
        return item
        

    def top(self) -> int:
        
        return self.stk[-1]


    def empty(self) -> bool:
        
        if len(self.stk) <= 0:
            return True

        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()