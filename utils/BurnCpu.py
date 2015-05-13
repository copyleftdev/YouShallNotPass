import multiprocessing
import math
import random


def worker():
    print("Worker")
    x = 0
    rand_list = []
    while x < 100000000000000000:

        print(x)
        p = x*math.pi
        p2 = math.sqrt(x**2 + p**2)
        for i in range(10000000):
            rand_list.append(random.randint(200003,9999999))

        for ele in rand_list:
            ele ** math.pi


        print(p2)

        x += 1
    return

if __name__ == '__main__':
    jobs = []
    for i in range(50):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
