import multiprocessing
from multiprocessing import Process, Pool
from time import perf_counter, sleep


def slow(name):
    print(f"Starting {name}")
    sleep(2)
    print(f"Ending {name}")


names = ['1th', '2th', '3th', '4th', '5th', '6th', '7th', '8th', '9th', '10th']

start = perf_counter()

pool = Pool(processes=2)
pool.map(slow, names)
pool.close()
pool.join()

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
