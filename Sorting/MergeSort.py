def mergeSort(input):
    if len(input)==0 or len(input)==1:
        return input
    else:
        mid=len(input)//2
        a=mergeSort(input[:mid])
        b=mergeSort(input[mid:])
        return merge(a,b)
def merge(a,b):
    templist=[]
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            templist.append(a[0])
            a.pop(0)
        else:
            templist.append(b[0])
            b.pop(0)
    if len(a)==0:
        templist=templist+b 
    else:
        templist=templist+a
    return templist 
def testSorting(input):
    return mergeSort(input)
    
    for idx in range(0,len(input)-1):
        assert(input[idx] <= input[idx+1])
testSorting([35,20,30,15,98,9,69,75,16,45,60])