###############全局解释器锁 GIL


from threading import Thread,Lock
import time

n = 1000


def task1():
    global n
    for i in range(100):
        n -= 1


def task2():
    global n
    for i in range(100):
        n -= 1


# if __name__ == '__main__':
#     t1 = Thread(target=task1)
#     t2 = Thread(target=task2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(n)  #### 800

#################### 如果运算量大，全局解释器锁GIL就会自动解锁了
i = 0


def add():
    global i
    for j in range(1000000):
        i += 1


# if __name__ == '__main__':
#     t1 = Thread(target=add)
#     t2 = Thread(target=add)
#     t3 = Thread(target=add)
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     print(i) ###2430390 不是3百万。应为计算量大,GIL锁自动解锁了。


##################计算量大，GIL锁自动解锁，我们给他加锁
j = 0
lok = Lock()
def add2():
    global j
    lok.acquire()
    for k in range(1000000):
        j += 1
    lok.release()

if __name__ == '__main__':
    t1 = Thread(target=add2())
    t2 = Thread(target=add2())
    t3 = Thread(target=add2())
    t1.start()
    t2.start()
    t3.start()
    print(j) ###3000000,就很准确
    print("END")
