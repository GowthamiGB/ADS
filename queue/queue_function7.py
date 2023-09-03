from queue7 import *
s1=FindMaxElement()
assert(s1.q1.enqueue(40)==1)
assert(s1.q1.enqueue(10)==2)
assert(s1.q1.enqueue(30)==3)
assert(s1.findMax()==40)
assert(s1.q1.deque()==40)
assert(s1.findMax()==30)