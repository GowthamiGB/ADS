from sll1 import *
def split(s1,s2):
    cur=s1.head
    next=cur.next
    while  cur!=None and next!=None:
        if(next!=None):
            cur.next=next.next
            cur=next.next
        s2.addAtTail(next.data)
        if(cur!=None):
            next.next=cur.next
            next=next.next
        return(s1.getElements(),s2.getElements())

s1=SList()
s2=SList()
for i in range(1,9):
    s1.addAtTail(i)
assert(split(s1,s2)==([1,3,5,7],[2,4,6,8]))

