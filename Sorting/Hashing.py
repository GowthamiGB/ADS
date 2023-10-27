import numpy as np
class extHash:
    class _node_:
        def __init__(self,id,name):
            self.id=id
            self.name=name
            self.next=None
        tableSize=11
    def __init__(self):
        hashTable=[None]*extHash.tableSize
        self.p=13
        self.a=np.random.randint(1,self.p-1)
        self.b=np.random.randint(0,self.p-1)
    def _hashcode_(self,element):
        hashcode=0
        for ch in element:
            hashcode=hashcode << 5
            hashcode=hashcode+ord(ch)
        return hashcode
    def _compress_(self,hashcode):
        return (((hashcode*self.a+self.b)%self.p)%extHash.tableSize)
    def _hash_(self,element):
        hashcode=_hashcode_(element)
        tableIndex=_compress_(hashcode)
        return tableIndex
    def _isMember_(self,id):
        bIndex=self._hash_(id)
        node=self.hashTable[bIndex]
        while node:
            if node.id==id:
                break
            else:
                node=node.next
        return node!=None
    def addElement(self,id):
        if not self._isMember_(id):
            bIndex=self._hash_(id)
            oldAdd=self.hashTable[bIndex]
            node=self._node_(id,name)
            node.next=oldAdd
            self.hashTable[bIndex]=node
    def deleteElement(self,id):
        bIndex=self._hash_(id)
        if self.hashTable[bIndex]:
            if self.hashTable[bIndex].id==id:
                self.hashTable[bIndex]=self.hashTable[bIndex].next
            else:
                node=self.hashTable[bIndex]
                while node.next!=None:
                    if node.next.id==id:
                        node.next=node.next.next
                    else:
                        node=node.next
    def printHashTable(self):
        for idx in range(0,extHash.tableSize):
            node=self.hashTable[idx]
            while node:
                print(node.id)
                print(node.name)
                node=node.next
            print( )

hash=extHash()
hash.addElement(1,Gowth)
hash.addElement(2,Nidhi)
hash.addElement(3,Mouna)
hash.addElement(4,Bindu)
print(hash.printHashTable())