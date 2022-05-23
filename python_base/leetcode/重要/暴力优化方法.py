####### 方法一：使用 functools.lru_cache装饰器。可以缓存数值，加快运行速度 #####

## 定义一个装饰器，查看程序运行的时间
import time
from unittest import FunctionTestCase

from youtube_dl import main


# def countTime(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         print("运行时间",end-start)
#     return wrapper
    

### 写一个  斐波那契数 ,看看 优化效果
# @countTime

def feibona(n):
    ### 递归
    ## 出口
    if n <2:
        return 1
    return feibona(n-2) + feibona(n-1)

#### 添加 functions.lru_cache 装饰器
import functools
@functools.lru_cache()
def feibona2(n):
    if n < 2:
        return n
    return feibona2(n-1) + feibona2(n-2)



if __name__ == '__main__':
    start_time = time.time()
    # res = feibona(20) ### 0.00200
    res = feibona2(20) ###
    end_time = time.time() ###0.00000   速度变快了
    
    detaTime = end_time-start_time
    print(res,"%.5f" % detaTime)



