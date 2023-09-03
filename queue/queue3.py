# FlexiQueue with capacity to expand and shrunk based on elements to be added or deleted
class FlexiQueue:
    defaultSize=2 #set default size as 2
    def __init__(self):
        self.data=[None]*FlexiQueue.defaultSize
        self.front=0
        self.count=0
    def length(self):
        return self.count #to get the count
    def isEmpty(self):
        return self.count==0
    def getFirst(self): #to get the first element
        if not self.isEmpty():
            return self.data[self.front]
        else:
            return None
    def enqueue(self, ele): #to add element
        if self.count==len(self.data):
            self.resize(2*len(self.data)) #resize-2*2
        idx=(self.front+self.count)%len(self.data) 
        self.data[idx]=ele #add element to that index
        self.count+=1 #increment the count
        return self.count
    def dequeue(self): #to delete element
        if not self.isEmpty():
            ele=self.data[self.front] 
            self.count-=1 
            self.data[self.front]=None #delete 
            self.front=(self.front+1)%len(self.data) 
            if 0<len(self.data)//4: #length divide
                self.resize(len(self.data)//2)
            return ele
        else:
            return None
    def resize(self,cap): #resize the list using capactity
        oldData=self.data
        walk=self.front
        self.data=[None]*cap
        for k in range(self.count):
            self.data[k]=oldData[walk]
            walk=(walk+1)%len(oldData)
        self.front=0

    def getSize(self): #to get size of the list
        return len(self.data)
