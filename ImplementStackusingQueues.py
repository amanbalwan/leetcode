class MyStack:

    def __init__(self):
        self.s=[]
        

    def push(self, x: int) -> None:
        
        self.s.append(x)
        return self.s

    def pop(self) -> int:
        
        return self.s.pop(-1)
        

    def top(self) -> int:
        return self.s[-1]
        
        

    def empty(self) -> bool:
        if self.s:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()