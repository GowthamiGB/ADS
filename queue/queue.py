# implement simple queue using list data structure
class simpleQueue:
    def __init__(self): #initialize
        self.data=[]
        self.count=0

    def isQueueEmpty(self): #to check if queue is empty
        return self.count==0

    def getElementCount(self): #to get count
        return self.count

    def enqueue(self,ele): #to add element at the end
        self.data.append(ele)
        self.count+=1
        return self.count
    
    def deque(self): #to delete element
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None

    def peek(self): #to get last element
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
    
    def printElements(self):
        return self.data
    
