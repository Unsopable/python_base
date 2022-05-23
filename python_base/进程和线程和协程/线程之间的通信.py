import queue
import threading
import time
import random


def product(q):
    i = 0
    while i < 6:
        num = random.randint(0,100)
        q.put(num)
        print("生产者生产了：{}".format(num))
        time.sleep(1)
        i+=1
    q.put(None)
    q.task_done()


def consum(q):
    while True:
        n = q.get()
        if n == None:
            break
        print("消费者消费了: %d" %n)
        time.sleep(3)

    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(6)
    t1 = threading.Thread(target=product, args=(q,))
    t2 = threading.Thread(target=consum, args=(q,))
    t1.start()
    t2.start()