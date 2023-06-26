# FIFO = First In First Out (Queue)
# LIFO = Last In First Out  (Stack)

from multiprocessing import Queue

queue = Queue()

queue.put(1)
queue.put(2)
queue.put(3)

# 1,2,3


el1 = queue.get() # 1
print(queue.qsize())


# print(el1,el2,el3)
