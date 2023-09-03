# from queue3 import*
# def testEmptyQueue():
#     s1=flexiQueue()
#     assert(s1.length()==0)
#     assert(s1.isEmpty()==True)

# def testEnqueue():
#     s2=flexiQueue()
#     s2.enqueue(10)
#     assert(s2.length()==1)

# def testDeque():
#     s3=flexiQueue()
#     s3.enqueue(20)
#     s3.enqueue(30)
#     assert(s3.length==2)
#     s3.enqueue(40)
#     assert(s3.length()==3)
#     assert(s3.deque()==20)
#     assert(s3.length()==2)
#     assert(s3.dequeue()==30)
#     assert(s3.length()==1)
#     assert(s3.deque()==40)
#     assert(s3.length()==0)

# testEmptyQueue()
# testEnqueue()
# testDeque()

class FlexiQueue:
    defaultSize=2
    def __init__(self):
        self.data=[None]*FlexiQueue.defaultSize
        self.front=0
        self.count=0
    def length(self):
        return self.count
    def isEmpty(self):
        return self.count==0
    def getFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
        else:
            return None
    def enqueue(self, ele):
        if self.count==len(self.data):
            self.resize(2*len(self.data))
        idx=(self.front+self.count)%len(self.data)
        self.data[idx]=ele
        self.count+=1
        return self.count
    def dequeue(self):
        if not self.isEmpty():
            ele=self.data[self.front]
            self.count-=1
            self.data[self.front]=None
            self.front=(self.front+1)%len(self.data)
            if 0<len(self.data)//4:
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
            walk=(walk+1)%len(oldData)
        self.front=0

    def getSize(self):
        return len(self.data)
