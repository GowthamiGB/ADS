from queue2 import *
def testEmptyQueue():
    q1=limitedQueue()
    assert(q1.getElementCount()==0)
    assert(q1.isQueueEmpty()==True)
    assert(q1.isQueueFull()==False)

def testEnqueue():
    q2=limitedQueue()
    q2.enqueue(10)
    assert(q2.getElementCount()==1)
    assert(q2.printElements()==[10,None,None,None,None])
    assert(q2.peek()==10)

def testDeque():
    q3=limitedQueue()
    q3.enqueue(20)
    q3.enqueue(30)
    q3.enqueue(40)
    q3.enqueue(50)
    q3.enqueue(60)
    assert(q3.getElementCount()==5)
    assert(q3.isQueueFull()==True)
    assert(q3.peek()==60)
    assert(q3.deque()==20)
    assert(q3.getElementCount()==4)
    assert(q3.printElements()==([30,40,50,60]))

testEmptyQueue()
testEnqueue()
testDeque()