from multiprocessing import Pool
import time
import random


##任务
def task(task_name):
    print('开始做任务啦', task_name)
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print("用时：", end - start)


if __name__ == '__main__':
    ###创建进程池(有5个进程)
    pool = Pool(5)
    tasks = ['听音乐','洗衣服','吃饭','打游戏','散步','看孩子']
    for t in tasks:
        pool.apply_async(task,args=(t,))
    ###挡住主进程结束，主线结束，进程池也结束了。（必须加）
    pool.close()
    pool.join()

    print("over!!!")