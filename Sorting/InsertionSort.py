def insertionSort(input):
    for i in range(1,len(input)):
        j=i-1
        key=input[i]
        while j>=0 and key<input[j]:
            input[j+1]=input[j]
            j-=1
        input[j+1]=key
    print(input)
def testSorting(input):
    insertionSort(input)
    for idx in range(0,len(input)-1):
        assert(input[idx] <= input[idx+1])
testSorting([64, 34, 25, 12, 22, 11, 90])