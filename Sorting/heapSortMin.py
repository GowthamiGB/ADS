# 3. Build minimum heap with required methods. It should support the behaviors like adding element, 
# getting minimum element, extracting minimum element, count number of elements and to check 
# the method to test the heap order property.
# 4. Modify Q3 to sort the input in descending order.
class minHeap:
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
                if self.data[right]<self.data[left]:
                    bigchild=right
            if self.data[bigchild]<self.data[idx]:
                self._swap_(bigchild,idx)
                self._downHeap_(bigchild,length)
    def addElement(self,key):
        self.data.append(key)
        self._upHeap_(len(self.data)-1)
    def _upHeap_(self,j):
        parent=self._parent_(j)
        if j>0 and self.data[j]<self.data[parent]:
            self._swap_(j,parent)
            self._upHeap_(parent)

    #Getting the minimum element
    def minElement(self):
        return self.data[0]  
    #Deleting the min element
    def deleteMin(self):
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
heap=minHeap()
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
heap.minElement()
assert(heap.count()==10)
assert(heap.minElement()==5)
assert(heap.deleteMin()==5)
assert(heap.minElement()==15)
assert(heap.deleteMin()==15)
assert(heap.minElement()==20)
assert(heap.heapSort()==([90,85,75,65,45,35,25,20]))