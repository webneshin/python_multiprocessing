import multiprocessing
from multiprocessing import Process
from time import perf_counter, sleep


def slow(name):
    print(f"Starting {name}")
    sleep(2)
    print(f"Ending {name}")


start = perf_counter()

p1 = Process(target=slow, args=("First",))
p2 = Process(target=slow, args=("Second",))

p1.start()
p2.start()

p1.join()
p2.join()

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
