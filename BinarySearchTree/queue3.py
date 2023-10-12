class flexiQueue:
    defaultSize=2
    def __init__(self):
        self.data=[None]*flexiQueue.defaultSize
        self.count=0
        self.front=0
    def length(self):
        return self.count
    def isEmpty(self):
        return self.count==0
    def getFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
        else:
            return None
    def enqueue(self,ele):
        if self.count==len(self.data):
            self.resize(2*len(self.data))
        idx=(self.front+self.count) % len(self.data)
        self.data[idx]=ele
        self.count+=1
    def dequeue(self):
        if not self.isEmpty():
            ele=self.data[self.front]
            self.count-=1
            self.data[self.front]=None
            self.front=(self.front+1)%len(self.data)
            if len(self.data)//4:
                self.resize(len(self.data)//2)
            return ele
        else:
            return None

    def resize(self,cap):
        oldData=self.data
        walk=self.front
        self.data=[None]*cap
        for k in range(self.count):
            self.data[k]=oldData[walk]
            walk=(walk+1)%(len(oldData))
