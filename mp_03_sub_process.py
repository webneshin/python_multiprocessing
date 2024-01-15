import multiprocessing
from multiprocessing import Process
from time import perf_counter, sleep


def slow(name):
    print(f"Starting {name}")
    sleep(2)
    print(f"Ending {name}")


class SlowProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        slow(self.name)


start = perf_counter()

p1 = SlowProcess("First")
p2 = SlowProcess("Second")

p1.start()
p2.start()

p1.join()
p2.join()

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
