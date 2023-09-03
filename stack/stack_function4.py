from stack4 import*
def testApp():
    stk=stack()
    f_read=open('_','r')
    data=f.f_read.read()
    f_read.close()
    assert(testSymbols(data,stk)==True)