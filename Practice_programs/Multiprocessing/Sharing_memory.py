from multiprocessing import Process, Value, Array

__author__ = 'gauth_000'


def f(val, num):
    val.value = 2
    num[:] = list(map(lambda x: x ** 2, num))


if __name__ == '__main__':
    val = Value('d', 0.0)
    num = Array('i', range(10))
    p = Process(target=f, args=(val, num))
    p.start()
    p.join()
    print('value:', val.value)
    print('num:', num[:])
