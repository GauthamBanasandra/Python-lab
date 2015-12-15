from multiprocessing import Process, Queue

__author__ = 'gauth_000'


def f(q):
    q.put([1, 2, 3, 'queue'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
