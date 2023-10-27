# 1. Build maximum heap with required methods. It should support the behaviors like adding element, 
# getting maximum element, extracting maximum element, count number of elements and to check 
# the method to test the heap order property.
# 2. Modify Q1 to sort the input in ascending order.
class maxHeap:
    def __init__(self,lst=[]):
        self.data=lst
        self._buildHeap_()
    def isEmpty(self):
        return len(self.data)==0
    def _parent_(self,idx):
        return (idx-1)//2
    def _lchild_(self,idx):
        return (2*idx+1)
    def _rchild_(self,idx):
        return (2*idx+2)
    def count(self):
        return len(self.data)
    def _swap_(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]
    def _buildHeap_(self):
        length=len(self.data)
        start=(length-2)//2
        for idx in range(start,-1,-1):
            self._downHeap_(idx,length)
    def _downHeap_(self,idx,length):
        if self._lchild_(idx)<length:
            left=self._lchild_(idx)
            bigchild=left
            if self._rchild_(idx)<length:
                right=self._rchild_(idx)
                if self.data[right]>self.data[left]:
                    bigchild=right
            if self.data[bigchild]>self.data[idx]:
                self._swap_(bigchild,idx)
                self._downHeap_(bigchild,length)
    def addElement(self,key):
        self.data.append(key)
        self._upHeap_(len(self.data)-1)
    def _upHeap_(self,j):
        parent=self._parent_(j)
        if j>0 and self.data[j]>self.data[parent]:
            self._swap_(j,parent)
            self._upHeap_(parent)

    #Getting the maximum element
    def maxElement(self):
        return self.data[0]  
    #Deleting the max element
    def deleteMax(self):
        ele=self.data[0]
        self._swap_(0,len(self.data)-1)
        self.data.pop()
        self._downHeap_(0,len(self.data))
        return ele
    #Method to test the heap order property     
    def heapSort(self):
        if not self.isEmpty():
            for idx in  range(len(self.data)-1,0,-1):
                self._swap_(0,idx)
                self._downHeap_(0,idx)
        return self.data
heap=maxHeap()
heap.addElement(15)
heap.addElement(20)
heap.addElement(45)
heap.addElement(75)
heap.addElement(35)
heap.addElement(65)
heap.addElement(25)
heap.addElement(85)
heap.addElement(5)
heap.addElement(90)
heap.maxElement()
assert(heap.count()==10)
assert(heap.maxElement()==90)
assert(heap.deleteMax()==90)
assert(heap.maxElement()==85)
assert(heap.deleteMax()==85)
assert(heap.maxElement()==75)
assert(heap.heapSort()==([5,15,20,25,35,45,65,75]))