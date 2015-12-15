from multiprocessing import Process, Pipe

__author__ = 'gauth_000'


def f(conn):
    conn.send('Hello from child process')


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    child_process = Process(target=f, args=(child_conn,))
    child_process.start()
    print(parent_conn.recv())
    child_process.join()
