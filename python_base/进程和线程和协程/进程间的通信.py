from multiprocessing import Process, Queue
import time


def download(q):
    imgs = ['girl.jpg', 'main.jpg', 'boy.jpg']
    for img in imgs:
        time.sleep(1)
        print('{}下载完成'.format(img))
        q.put(img)
    # q.task_done()

def getfile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print("{}保存成功".format(file))
        except:
            print("全部保存完毕")
            break
    # q.task_done()###c错误，没有task_done()
if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    #####  join() 用于阻止主线程结束；防止：主线程执行结束， 但是子线程还在运行。
    p1.join()
    p2.start()
