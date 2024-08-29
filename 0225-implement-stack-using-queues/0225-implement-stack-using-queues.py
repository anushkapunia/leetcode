class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
        

    def push(self, x):
        self.q1.append(x)
        

    def pop(self):
        if len(self.q1) == 0: return -1 
        
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
            
        p = self.q1.popleft()
        
        while self.q2:
            self.q1.append(self.q2.popleft())
            
        return p
        

    def top(self):
        return self.q1[len(self.q1)-1]
   
        

    def empty(self):
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()