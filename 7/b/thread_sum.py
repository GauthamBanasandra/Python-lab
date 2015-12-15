import random
import threading as t

__author__ = 'gauth_000'


def add(*numbers):
    global total_sum
    res = sum(numbers)
    l.acquire()
    total_sum += res
    l.release()


total_sum = 0
l = t.Lock()
numbers = [random.randint(1, 10) for i in range(10)]
size = len(numbers)
t1 = t.Thread(target=add, args=numbers[:size // 4])
t2 = t.Thread(target=add, args=numbers[size // 4:size // 2])
t3 = t.Thread(target=add, args=numbers[size // 2:3 * size // 4])
t4 = t.Thread(target=add, args=numbers[3 * size // 4:size])
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(numbers, 'sum=' + str(sum(numbers)), 'total_sum=' + str(total_sum), sep='\n')
