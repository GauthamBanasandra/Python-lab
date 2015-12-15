from multiprocessing import Process, Manager
import multiprocessing as mp
import os
__author__ = 'gauth_000'


def f(d, l):
    d[1] = 'one'
    d[2] = 'two'
    l.reverse()
    print('pid:', os.getpid())
    while True:
        pass

if __name__ == '__main__':
    mp.set_start_method('spawn')
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    p = Process(target=f, args=(d, l))
    p.daemon = True
    p.start()
    mp.current_process().terminate()
    p.join()
    print(d)
    print(l)