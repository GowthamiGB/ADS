def bubbleSort(input):
    for i in range(0,len(input)-2):
        for j in range(len(input)-1,i,-1):
            if input[j]<input[j-1]:
                input[j],input[j-1]=input[j-1],input[j]
    print(input)  
def testSorting(input):
    bubbleSort(input)
    for idx in range(0,len(input)-1):
        assert(input[idx] <= input[idx+1])
testSorting([64, 34, 25, 12, 22, 11, 90])