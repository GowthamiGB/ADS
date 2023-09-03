import random
import string
# SAMPLE 2

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
# 

#Program to find union of 2 list
def union(a,b):
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
    return sorted(c)

#Program to find intersection of 2 list
def intersection(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c

#Program to find union and intersection without repetition
def unionintersection(a,b):
    unionList=set(union(a,b))
    intersectionList=set(intersection(a,b))
    return unionList,intersectionList

#Program to create list of 2 tuples 1st number and the square of the number
def squarenumbertuple(n):
    a=[]
    for i in range(1,n+1):
        a.append((i,i**2))
    return a

#Program to remove duplicates from list
def removeDuplicates(a):
    index = 0
    while index < len(a):
        element = a[index]
        if a.count(element) > 1:
            a.remove(element)
        else:
            index += 1
    return a

#Program to find the longest lenght word in a list and return the length
def findLongestLenghtWord(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


#Program to add key value pair to dictionary
def addKeyValue(dictionary,key,value):
    dictionary[key]=value
    return dictionary

#Program to concatenate 2 dictionaries
def concat(dict1,dict2):
    concat_dict={**dict1,**dict2}
    return concat_dict

#Program to check if key exists in dictionary
def ifKeyPresent(dict,key):
    if key in dict:
        return True
    else:
        return False

#Program to generate dictionary in i, i^2 format
def power(n):
    dict={}
    for i in range(1,n+1):
        dict[i]=i**2
    return dict

#Program to sum all values in a dictionary
def sumValue(dict):
    total=sum(dict.values())
    return total

#Program to multiply all values
def multiply(dict):
    product=1
    for value in dict.values():
        product*=value
    return product

#Program to remove a key
def remove(dict,key):
    if key in dict:
        del dict[key]
    return dict

#Program to check if dictionary is empty
def is_empty(my_dict):
    return not bool(my_dict)

#Program to create dictionary from tuples
def makeDict(tuple):
    dict = {}
    for key, value in tuple:
        dict[key] = value
    return dict

#Program for encrypted string
def encryption(dict,a):
    b=[]
    for i in a:
        b.append(dict[i])
    return ''.join(b)

#Program to generate random dictionary
def randomDict(a):
    dict={}
    original_alphabet=list(string.ascii_letters)
    shuffled_alphabet = original_alphabet.copy()
    random.shuffle(shuffled_alphabet)
    for original,encrypted in zip(original_alphabet,shuffled_alphabet):
        dict[original]=encrypted
    b=encryption(dict,a)
    return b

#Program to convert marks to grade
def marksToGrade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'

#Program to convert marks to grade in dictionary  
def newDictWithGrade(dict):
    a=[]
    for student,subject_marks in dict.items():
        grades={}
        for subject,marks in subject_marks.items():
            grades[subject]=marksToGrade(marks)
        dict[student]=grades
    return dict


