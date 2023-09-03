from queue import *
from stack import*
#Queue using stacks
class QueueusingStacks:
    def __init__(self):
        self.s1=stack()
        self.s2=stack()
        #to add into queue
    def enqueue(self,ele):
        self.s1.push(ele)
        return self.s1.count
        #to remove element from s1 and pop to s2.wait until last element then pop
    def deque(self):
        while(self.s1.getElementCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.pop()
        while(self.s2.getElementCount()>0):
            self.s1.push(self.s2.pop())
        return ele
        #to return the first element
    def peek(self):
        while(self.s1.getElementCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.peek()
        self.s2.push(self.s1.pop())
        while(self.s2.getElementCount()>0):
            self.s1.push(self.s2.pop())
        return ele
