class SimpleStack:
    def __init__ (self):
        self.data=[]
        self.count=0
    def getElementCount(self):
        return self.count
    def isStackEmpty(self):
        return self.count==0
    def stackPush(self,ele):
        self.data.append(ele)
        self.count+=1
    def stackPop(self):
        if not self.isEmpty():
            self.count=-1
            return self.data.pop()
        else:
            return None
    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return None
    def printElement(self):
        return self.data[0:]
            