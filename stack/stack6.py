# Implement a function with signature transfer(S,T).This function transfers elements from S to T. The sequence of elements
# in T should be same as S.

from stack import *

s=stack()
t=stack()

def transfer(S,T):
    #A temporary stack is created for storing the data from stack S while copying to T to maintain the same order of data
    temp=stack()
    while(s.getElementCount()>0):
        temp.push(s.pop())
    while(temp.getElementCount()>0):
        t.push(temp.pop())
    return t.printElements()


s.push(10)
s.push(20)
s.push(30)
s.push(40)
assert(transfer(s,t)==([10,20,30,40]))