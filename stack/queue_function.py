from queue import *
def testEmptyQueue():
    q1=simpleQueue()
    assert(q1.getElementCount()==0)
    assert(q1.isQueueEmpty()==True)

def testEnqueue():
    q2=simpleQueue()
    q2.enqueue(10)
    assert(q2.getElementCount()==1)
    assert(q2.peek()==10)

def testDeque():
    q3=simpleQueue()
    q3.enqueue(20)
    q3.enqueue(30)
    q3.enqueue(40)
    assert(q3.getElementCount()==3)
    assert(q3.peek()==40)
    assert(q3.deque()==20)
    assert(q3.getElementCount()==2)
    assert(q3.printElements()==[30,40])

testEmptyQueue()
testEnqueue()
testDeque()