from method import *

assert(swap(30,40)==(40,30))
assert(check(9).lower()==('positive number').lower())
assert(checkDivisor(20,4)==[4,8,12,16,20])
assert(Divide(40,5)==(8,0))
assert(oddNumbers(15)==[1,3,5,7,9,11,13,15])
assert(sumOfDegits(143)==8)
assert(findSmallestDivisor(35)==5)
assert(sumOfSeries(1,3)==123)
assert(reverse(143)==341)
assert(average([1,3,5,7,9])==5)
assert(count(12345)==5)
assert(palindrome(1234321)==True)
assert(ifSubStringFound("She is Nidhi. Nidhi is from TTH. Nidhi is pursuing masters in BDA.","Nidhi")==3)
assert(indexSubStringFound("She is Nidhi. Nidhi is from TTH. Nidhi is pursuing masters in BDA","Nidhi")==7)
assert(checkForCharacters("My")==True)
assert(replace("ananyaa ana")=="$n$ny$$ $n$")
assert(countVowels("asdfgeirouASDEBITOVU")==10)
assert(replaceBlankSpace("My name is  Nidhi")=="My-name-is--Nidhi")
assert(findLength("nidhi")==5)
assert(findLargerString("nidhi","Nidhi Shiravanthe")=="Nidhi Shiravanthe")
assert(countOfUpperLower("Nidhi S Rao")==(3,6))
assert(countCharsDigits("NidhiSRao123")==(9,3))
assert(fullPattern("Nidhi S Rao is from  Thirthahalli","Nidhi S Rao")==True)
assert(cumulative_Sum([1,2,4,5,7])==[1,3,7,12,19])
print(tenRandomNumbers())
print(tenRandomNumbersRange())
print(uniqueRandomNumbers())
print(randomNumbers())
