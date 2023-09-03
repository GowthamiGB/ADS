from queue5 import*
q1=QueueusingStacks()
assert(q1.enqueue(10)==1)
assert(q1.enqueue(20)==2)
assert(q1.enqueue(30)==3)
assert(q1.deque()==10)
assert(q1.peek()==20)