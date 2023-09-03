from function import *

assert(swap(20,30)==(30,20))
assert(isPositive(8)==True)
assert(checkDivisor(20,4)==[4,8,12,16,20])
assert(SumofDigits(12345)==15)
assert(Smallest(35)==5)
assert(sumOfSeries(1,3)==123)
assert(reverse(143)==341)
assert(average([1,3,5,7,9])==5)
assert(count(12345)==5)
assert(ifSubStringFound("I AM GOWTHAMI.GOWTHAMI IS STUDYING IN MANIPAL","GOW")==2)
assert(indexSubStringFound("I AM GOWTHAMI.GOWTHAMI IS STUDYING IN MANIPAL","GOW")==5)
assert(checkForCharacters("My")==True)
assert(replace("appleaa apple")=="$pple$$ $pple")
assert(vowels("abcdefghijklmnop")==4)
assert(BlankSpace("Gowthu Bhat")=="Gowthu-Bhat")
assert(length("Gowthu")==6)
assert(uppertolower("Gowthami G Bhat")==(3,10))
assert(countCharsDigits("Gowthami123")==(8,3))
assert(fullPattern("My name is Gowthami","Gowthami")==True)
assert(cumulative_Sum([1,2,4,5])==[1,3,7,12])
print((RandomNumbers()))
print(tenRandomNumbersRange())
print(uniqueRandomNumbers())
print(randomNumbers())



