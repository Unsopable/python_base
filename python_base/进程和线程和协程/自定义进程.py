from multiprocessing import Process


####自定义进程，只要重写run()函数

class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        n = 1
        while True:
            print('{}----->自定义进程，n:{}'.format(self.name, n))
            n += 1

if __name__ == '__main__':
    p1 = MyProcess('小明')
    p1.start()
    p2 = MyProcess('小红')
    p2.start()