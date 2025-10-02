class MinStack:

    def __init__(self):
        
        self.stk = []
        self.min_stk = []        

    def push(self, val: int) -> None:
        
        self.stk.append(val)

        if self.min_stk:
            val = min(val,self.min_stk[-1])
            self.min_stk.append(val)

        else:
            self.min_stk.append(val)


    def pop(self) -> None:
        
        item = self.stk.pop()
        self.min_stk.pop()
        return item

    def top(self) -> int:
        
        return self.stk[-1]

    def getMin(self) -> int:
        
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()