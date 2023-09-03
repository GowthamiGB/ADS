from queue4 import *

def StackQueue():
    s1=StackusingQueues()
    assert(s1.push(10)==1)
    assert(s1.push(20)==2)
    assert(s1.push(30)==3)
    assert(s1.pop()==30)
    assert(s1.peek()==20)