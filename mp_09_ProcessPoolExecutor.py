import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
from time import perf_counter, sleep


def slow(name):
    print(f"Starting {name}")
    sleep(2)
    print(f"Ending {name}")


def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        names = ['1th', '2th', '3th', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        executor.map(slow, names)


start = perf_counter()

main()

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
