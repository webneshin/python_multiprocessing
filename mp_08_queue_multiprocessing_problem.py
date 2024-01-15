from multiprocessing import Process

numbers = []


def p1_func():
    global numbers
    numbers.extend(list(range(1, 10)))
    print(numbers)


def p2_func():
    global numbers
    numbers.extend(list(range(11, 20)))
    print(numbers)


p1 = Process(target=p1_func)
p2 = Process(target=p2_func)

p1.start()
p2.start()

p1.join()
p2.join()

print(numbers)
