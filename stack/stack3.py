#to reverse  the content of the file
from stack import *
def reverse(file):
    s1=stack()
    with open(file,'r')as input_file: #open file in read mode
        for line in input_file:
            s1.push(line) #push line to s1
    input_file.close()
    with open(file,'w') as output_file: #give output with write mode
        while not s1.isStackEmpty():  
            output_file.write(s1.pop())  #write the output from stack using pop
    output_file.close()

reverse('sample.txt')