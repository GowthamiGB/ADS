from queue import *
#Stack usin two queues
class StackusingQueues:
    def __init__(self):
        self.q1=simpleQueue()
        self.q2=simpleQueue()
        #normal push function
    def push(self,ele):
        self.q1.enqueue(ele)
        return self.q1.count
        #take two queues and pop from q1 to q2 till last element thn pop
    def pop(self):
        while(self.q1.getElementCount()>1):
            self.q2.enqueue(self.q1.deque())
        ele=self.q1.deque()
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.deque())
        return ele
        #to check the topmost element
    def peek(self):
        while(self.q1.getElementCount()>1):
            self.q2.enqueue(self.q1.deque())
        ele=self.q1.peek()
        self.q2.enqueue(self.q1.deque())
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.deque())
        return ele
        


