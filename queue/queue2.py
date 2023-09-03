# Simple queue can contain limited number of elements
class limitedQueue:
    def __init__(self):
        self.count=0
        self.data=[None]*5 #limiting queue size
        self.front=-1
    
    def isQueueFull(self):
        return self.count>=len(self.data) #check if queue is full

    def isQueueEmpty(self): #to check if queue is empty
        return self.count==0

    def getElementCount(self): #to get number of elements in queue
        return self.count

    def enqueue(self,ele): #to add elements to the queue
        if not self.isQueueFull():
            self.front+=1
            self.data[self.front]=ele
            self.count+=1
            return self.count
        else:
            return None


    def deque(self): #to delete element from the queue
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None

    def peek(self): #to get the topmost element
        if not self.isQueueEmpty():
            return self.data[self.front]
        else:
            return None
    
    def printElements(self): #to print elements
        return self.data