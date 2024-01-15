import multiprocessing
import os
from multiprocessing import Process, current_process
from time import perf_counter, sleep


def slow(name):
    print("*" * 30)
    print(f"Starting {name}")
    print(current_process())
    print(current_process().name)
    print('os-process id: ', os.getpid())
    print('os-parent process id: ', os.getppid())
    sleep(2)
    print(f"Ending {name}")


start = perf_counter()

p1 = Process(target=slow, args=("First",))
p2 = Process(target=slow, args=("Second",))

print("is_alive before start:", p1.is_alive())

p1.start()
p2.start()

print("is_alive before finish:", p1.is_alive())

p1.join()
p2.join()

print("is_alive after finish:", p1.is_alive())

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
