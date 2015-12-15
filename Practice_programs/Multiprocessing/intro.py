import multiprocessing as mp
import os

__author__ = 'gauth_000'


def f(fname):
    print('function:', fname)
    print('pid:', os.getpid())
    print('ppid:', os.getppid())
    print()
    while True:
        pass

# f('main')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    p = mp.Process(target=f, args=('child',))
    p.start()