from stack1 import*
def testEmptyStack():
    s1=SimpleStack()
    assert(s1.getElementCount()==0)
    assert(s1.isStackEmpty()==True)
def testPush():
    s2=SimpleStack()
    s2.stackPush(10)
    assert(s2.getElementCount()==1)
    s2.stackPush(20)
    assert(s2.getElementCount()==2)
def testPop():
    s3=SimpleStack()
    assert(s3.stackPop()==20)
    assert(getElementCount()==1)
def testPeek():
    s4=SimpleStack()
    assert(s4.stackPeek()==10)
def output():
    s5=simpleStack()
    assert(s5.printElement()==[10])










testEmptyStack()