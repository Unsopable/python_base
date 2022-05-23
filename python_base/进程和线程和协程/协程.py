###greenlet

from greenlet import greenlet
import time


def a():
    for i in range(4):
        print("A", i)
        # g2.switch()
        ### 必须要用gevent.sleep()才行
        gevent.sleep(0.1)
        ### 用 time.sleep() 是错误的
        time.sleep(0.1)


def b():
    for i in range(4):
        print("B", i)
        # g3.switch()
        gevent.sleep(0.1)


def c():
    for i in range(4):
        print("C", i)
        # g1.switch()
        gevent.sleep(0.1)


# if __name__ == '__main__':
#     g1 = greenlet(a)
#     g2 = greenlet(b)
#     g3 = greenlet(c)
#
#     g1.switch()


#################### gevent #####
import gevent
from gevent import monkey

if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()
