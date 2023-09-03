class stack:
    # Unlimited size stack
    def __init__(self):
        self.count=0
        self.data=[]
        # to check if stack is empty
    def isStackEmpty(self):
        return self.count==0
        # to get count of the stack
    def getElementCount(self):
        return self.count
        # to add element
    def push(self,element):
        self.data.append(element)
        self.count+=1
        return self.count
        # to fremove element
    def pop(self):
        if not self.isStackEmpty():
            self.count-=1
            return self.data.pop()
        else:
            return None
            # to get the topmost element
    def peek(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            return None
            # to print elements
    def printElements(self):
        return self.data[0:]



    