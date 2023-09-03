from queue import*
#to find the max element and queue should be same as original
class FindMaxElement:
    def __init__(self):
        self.q1=simpleQueue()
        self.q2=simpleQueue()
        #to print elements
    def printElements(self):
        return self.printElements()
        #set max as zero then update if greater than max. And push to q2 so that it is same as q1
    def findMax(self):
        self.max=0
        while(self.q1.getElementCount()>0):
            ele=self.q1.deque()
            if(self.max<ele):
                self.max=ele
            self.q2.enqueue(ele)
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.deque())
        return self.max



