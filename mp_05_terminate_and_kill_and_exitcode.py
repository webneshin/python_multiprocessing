import multiprocessing
from multiprocessing import Process
from time import perf_counter, sleep

"""
هر دو terminate و kill برای بستن process استفاده می شود.
فرق این دو در ارسال سیگنال بستن process به سیستم عامل است.
در terminate از SIGTERM استفاده می شود و در kill از SIGKILL استفاده می شود.
"""


def slow(name):
    print(f"Starting {name}")
    if name == "3th":
        raise Exception("s")
    sleep(2)
    print(f"Ending {name}")


start = perf_counter()

p1 = Process(target=slow, args=("First",))
p2 = Process(target=slow, args=("Second",))
p3 = Process(target=slow, args=("3th",))
p4 = Process(target=slow, args=("4th",))

p1.start()
p2.start()
p3.start()
p4.start()

p1.terminate()
p2.kill()

p1.join()
p2.join()
p3.join()
p4.join()

print("terminate exitcode:", p1.exitcode)
print("kill exitcode:", p2.exitcode)
print("error code exitcode:", p3.exitcode)
print("ok exitcode:", p4.exitcode)

end = perf_counter()

print("*" * 10, end - start, "*" * 10)
