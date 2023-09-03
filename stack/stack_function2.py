from stack2 import *
def testEmptyStack():
    s1=LimitedStack()
    assert(s1.getElementCount()==0)
    assert(s1.isStackEmpty()==True)
    assert(s1.isStackFull()==False)

def testPush():
    s2=LimitedStack()
    s2.push(10)
    assert(s2.getElementCount()==1)

def testPop():
    s3=LimitedStack()
    s3.push(20)
    s3.push(30)
    s3.push(40)
    s3.push(50)
    s3.push(60)
    assert(s3.isStackFull()==True)
    assert(s3.getElementCount()==5)
    assert(s3.peek()==60)
    assert(s3.pop()==60)
    assert(s3.getElementCount()==4)
    assert(s3.printElements()==([20,30,40,50]))

testEmptyStack()
testPush()
testPop()