#### 自定义装饰器复习
import functools
import time


def decorator(func):
    print("装饰完成，计算运行时间")
    ### 装饰函数
    @functools.wraps(func) ### 加了它，print(count.__name__) 为count ，否则 print(count.__name__) 为wrapper
    def wrapper(*args,**kwargs):
        start = time.time()
        ### 调用被装饰的函数
        func(*args,**kwargs)
        end = time.time()
        delate_time = end - start
        print("运行时间是：",delate_time)
    return wrapper

##### 装饰该函数，看看它运行需要多长时间
@decorator
def count(n):
    for i in range(n):
        print(i)
        
count(10)
print(count.__name__)