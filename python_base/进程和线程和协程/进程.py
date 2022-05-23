from multiprocessing import Process
import time

def task1():
    while True:
        time.sleep(0.5)
        print('这是任务一')

def task2():
    while True:
        time.sleep(0.5)
        print('这是任务2')

if __name__ == '__main__':
    p1 = Process(target=task1)
    p1.start()
    p2 = Process(target=task2)
    p2.start()
    print('Over!!!')