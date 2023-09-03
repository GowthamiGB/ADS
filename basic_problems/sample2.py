from function2 import *

# 1st
# list=[1,2,3,4,5]
# print("Largest element is:",max(list))

# 2nd
# list=[10,33,2,1,3,5]
# even=[]
# odd=[]
# for i in list:
#   if(i%2==0):
#    even.append(i)
#   else:
#     odd.append(i)
#   print("Even list is:",even)
#   print("Odd list is:",odd)

  #3rd using assert
# def exchange_values(val1,val2):
#     val1,val2=val2,val1 
#     return val1,val2
# assert(exchange_values(100,20)==(20,100))

# 3rd not using assert
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# a=a+b
# b=a-b
# a=a-b
# print("a is:",a)
# print("b is:",b)

# 4th
# list1=[10,20,30,40,50]
# list2=[10,20,30,50,40]
# list1.sort()
# list2.sort()
# if list1==list2:
#     print("The list are identical")
# else:
#     print("The list are not identical")

#5th
assert(union([1,2,3,4,5],[5,6,7,8,9])==[1,2,3,4,5,5,6,7,8,9])
assert(intersection([1,2,3,4,5],[1,2,8,9])==[1,2])
assert(unionintersection([1,2,3,4,5],[4,5,6])==({1,2,3,4,5,6},{4,5}))
assert(squarenumbertuple(3)==[(1,1),(2,4),(3,9)])
assert(removeDuplicates([1,2,4,2,1,3,5])==([4,2,1,3,5]))
assert(findLongestLenghtWord(["Gowthu","Gowthami G Bhat"])==15)


assert(addKeyValue({1:"Gowthami",2:"a"},3,"kite")==({1:"Gowthami",2:"a",3:"kite"}))
assert(concat({"name":"Gowthami"}, {"class":"PUC"})==({"name":"Gowthami","class":"PUC"}))
assert(ifKeyPresent({1:1,2:4,3:9},2)==True)
assert(power(4)=={1:1,2:4,3:9,4:16})
assert(sumValue({1:1,2:2,3:3})==6)
assert(multiply({1:1,2:2,3:3})==6)
assert(remove({1:1,2:4,3:9},2)==({1:1,3:9}))
assert(is_empty({})==True)
assert((makeDict([(1,1),(2,4)]))==({1:1,2:4}))
dict={'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 
'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 
'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 
'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': 
' ', 'w': 't'}
assert(encryption(dict,"cat")=="km ")

print(randomDict("GowthamiGBhat"))
print(newDictWithGrade({"GowthamiGBhat":{'ADS':80,'ABD':50},"ABC":{'ADS':40,'ABD':90}}))