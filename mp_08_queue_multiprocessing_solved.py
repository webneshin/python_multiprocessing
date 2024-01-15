from multiprocessing import Process, Queue

numbers = []


def p1_func(queue: Queue):
    nums = queue.get()
    nums.extend(list(range(1, 10)))
    queue.put(nums)
    print(nums)


def p2_func(queue: Queue):
    nums = queue.get()
    nums.extend(list(range(11, 20)))
    queue.put(nums)
    print(nums)


qs = Queue()
qs.put(numbers)

p1 = Process(target=p1_func, args=(qs,))
p2 = Process(target=p2_func, args=(qs,))

p1.start()
p2.start()

p1.join()
p2.join()

print(qs.get())
