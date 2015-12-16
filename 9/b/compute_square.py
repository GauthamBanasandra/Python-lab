import multiprocessing as mp
__author__ = 'gauth_000'
def square(v):
    print(v.value**2)
if __name__=='__main__':
    v=mp.Value('i', 2)
    p=mp.Process(target=square, args=(v,))
    p.start()
    p.join()