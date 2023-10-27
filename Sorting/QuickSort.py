def quickSort(input):
 
    start=0
 
    end=len(input)-1
 
    _quickSort_(input,start,end)
 
    return input
 
def _quickSort_(input,start,end):
 
    if start<end:  
 
        mid=_partition_(input,start,end)
 
        _quickSort_(input,start,mid-1)
 
        _quickSort_(input,mid+1,end)
 
def _partition_(input,start,end):
 
    up=start
 
    down=end
 
    pivot=input[start]
 
    while up<=down:
 
        while up<=down and input[up]<=pivot:
 
            up+=1
 
        while up<=down and input[down]>pivot:
 
            down-=1
        if(up<=down):
            input[up],input[down]=input[down],input[up]
 
    input[start],input[down]=input[down],input[start]
 
    return down
 
 
 
def testSorting(input):
 
    return quickSort(input)
 
    for idx in range(0,len(input)-1):
        assert(input[idx] <= input[idx+1])
 
print(testSorting([35,20,30,15,98,9,69,75,16,45,60]))