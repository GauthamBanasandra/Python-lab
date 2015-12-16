import multiprocessing as mp

__author__ = 'gauth_000'


def child(p, q):
    print(p.recv(), q.get(), sep='\n')


if __name__ == '__main__':
    c, p = mp.Pipe()
    q = mp.Queue()
    pr = mp.Process(target=child, args=(p, q))
    c.send('message through pipe')
    q.put('message through queue')
    pr.start()
    pr.join()
