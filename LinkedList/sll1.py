#Implementation of Singly Linked List with all conditions
class SList:
    class _Node:
        #Creating a node
        def __init__(self,ele):
            self.data=ele
            self.next=None
            #Initializing the head and tail information
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
        #Checking if the list is empty
    def isEmpty(self):
        return self.count==0
         #Getting the count of nodes in the list
    def listCount(self):
        return self.count
        #Adding a node at head
    def addAtHead(self,ele):
        new_node=self._Node(ele)
        if not self.isEmpty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
#Adding a new node at tail of the list
    def addAtTail(self,ele):
        new_node=self._Node(ele)
        if not self.isEmpty():
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
        return self.count
#Deleting a node at head of the list
    def deleteAtHead(self):
        if not self.isEmpty():
            data=self.head.data
            self.head=self.head.next
            if(self.head==None):
                self.tail=None
            self.count-=1
            return data
        else:
            return None
#Deleting a node at tail of the list
    def deleteAtTail(self):
        if not self.isEmpty():
            data=self.tail.data
            if (self.count>=1):
                last=self.tail
                cur=self.head
                while(cur.next!=last):
                    cur=cur.next
                self.tail=None
                cur.next=None
            else:
                self.head=self.tail=None
            self.count-=1
            return last.data
        else:
            return None
    #Checking if a given key present in the linked list
    def isMember(self,key):
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                if(cur.data==key):
                    break
                else:
                    cur=cur.next
            return cur!=None
        else:
            return None
    #Adding a node after a given node
    def addAfterNode(self,key,ele):
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                if(cur.data==key):
                    break
                else:
                    cur=cur.next
            if(cur!=None):
                new_node=self._Node(ele)
                new_node.next=cur.next
                cur.next=new_node
                if cur==self.tail:
                    self.tail=new_node
                self.count+=1
            else:
                print("Key not found")

        else:
            print("list is empty")
#Deleting a node after a given node
    def deleteAfterNode(self,key):
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                if(cur.data==key):
                    temp=cur.next
                    if(temp!=None):
                        next=temp.next
                        if(next!=None):
                            cur.next=next
                            self.count-=1
                            break
                        else:
                            cur.next=None
                            self.tail=cur
                            self.count-=1
                            break
                    else:
                        return None
            else:
                cur=cur.next
        else:
            return None

    def getElements(self):
        list=[]
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                list.append(cur.data)
                cur=cur.next
            return list

slist=SList()
slist.addAtHead(10)
slist.addAtTail(20)
slist.addAtHead(5)
slist.addAfterNode(10,15)
assert(slist.getElements()==([5,10,15,20]))
slist.addAfterNode(20,25)
assert(slist.getElements()==([5,10,15,20,25]))
assert(slist.deleteAtHead()==5)
assert(slist.deleteAtTail()==25)
assert(slist.getElements()==([10,15,20]))
# assert(slist.deleteAfterNode(10)==15)
# assert(slist.getElements()==([10,20]))
assert(slist.isMember(10)==True)