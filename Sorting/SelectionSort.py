def SelectionSort(input):
    for i in range(0,len(input)-2):
        pos=i
        for j in range(i+1,len(input)):
            if input[j]<input[pos]:
                pos=j
        input[i],input[pos]=input[pos],input[i]
    print(input)
def testSorting(input):
    SelectionSort(input)
    for idx in range(0,len(input)-1):
        assert(input[idx] <= input[idx+1])
testSorting([64, 34, 25, 12, 22, 11, 90])