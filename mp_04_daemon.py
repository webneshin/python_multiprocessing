import multiprocessing
import sys
from multiprocessing import Process
from time import perf_counter, sleep


def slow(name):
    print(f"Starting {name}")
    sleep(2)
    print(f"Ending {name}")


start = perf_counter()

p1 = Process(target=slow, args=("First",), daemon=True)
p2 = Process(target=slow, args=("Second",), daemon=True)

p1.start()
p2.start()

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
sys.exit()
