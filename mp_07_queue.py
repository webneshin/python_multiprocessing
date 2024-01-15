import queue

"""
https://docs.python.org/3/library/queue.html
سه نوع صف داریم
اولی Queue که از نوع FIFO می باشد. First in First Out
دومی LifoQueue که از نوع LIFO می باشد. Last in First Out
سومی PriorityQueue که اطلاعات را به ترتیب کوچکی و بزرگی مشخص می کند.
"""

fifo_q = queue.Queue()

fifo_q.put(1)
fifo_q.put(2)
fifo_q.put(3)

print("size:", fifo_q.qsize())
while not fifo_q.empty():
    print(fifo_q.get())


lifo_q = queue.LifoQueue()

lifo_q.put(1)
lifo_q.put(2)
lifo_q.put(3)

print("size:", lifo_q.qsize())
print(lifo_q.get())
print(lifo_q.get())
print(lifo_q.get())


p_q = queue.PriorityQueue()

p_q.put(4)
p_q.put(2)
p_q.put(3)

print("size:", p_q.qsize())
print(p_q.get())
print(p_q.get())
print(p_q.get())