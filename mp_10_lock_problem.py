import pickle
from multiprocessing import Process, Lock


def p1_func():
    for _ in range(10):
        n: int
        with open('mp_10_lock.pickle', 'rb') as f:
            n = pickle.load(f)
        with open('mp_10_lock.pickle', 'wb') as f:
            n += 1
            pickle.dump(n, f)


def p2_func():
    for _ in range(10):
        n: int
        with open('mp_10_lock.pickle', 'rb') as f:
            n = pickle.load(f)
        with open('mp_10_lock.pickle', 'wb') as f:
            n -= 1
            pickle.dump(n, f)


with open('mp_10_lock.pickle', 'wb') as f:
    pickle.dump(0, f)

p1 = Process(target=p1_func)
p2 = Process(target=p2_func)

p1.start()
p2.start()

p1.join()
p2.join()

with open('mp_10_lock.pickle', 'rb') as f:
    print(pickle.load(f))
