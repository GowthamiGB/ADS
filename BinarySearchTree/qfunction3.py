from queue3 import*
def testEmptyQueue():
    s1=flexiQueue()
    assert(s1.length()==0)
    assert(s1.isEmpty()==True)

def testEnqueue():
    s2=flexiQueue()
    s2.enqueue(10)
    assert(s2.length()==1)

def testDeque():
    s3=flexiQueue()
    s3.enqueue(20)
    s3.enqueue(30)
    assert(s3.length()==2)
    s3.enqueue(40)
    assert(s3.length()==3)
    assert(s3.dequeue()==20)
    assert(s3.length()==2)

testEmptyQueue()
testEnqueue()
testDeque()