###装饰器就是闭包的一种形式 (闭包要加一个接受函数的参数，就成装饰器了)



###### 内部函数
def func():
    a = 1
    b = [1,2,3]
    # print("a:{},b:{}".format(a,b))
    def inner_func():
        nonlocal a  ### 内部函数要更改外部函数的局部不可变参数时，要加nonlocal
        a = a + 1
        b.append(4)
    inner_func()
    print(a, b)
# func()

###### 闭包
def func1(f):
    print("----------")
    def func2():
        print("bbbbb")
    return func2
@func1
# a = func1()
# a()
### 闭包做个计数器
def counter_time():
    timer = [0]
    def add_1():
        timer[0] = timer[0] + 1
        print(timer[0])
    return add_1

# cunter = counter_time()
# cunter()
# cunter()
# cunter()

####### 装饰器(就是特殊的闭包)
def decorator(func):
    print("开始装饰")

    def wrapper():
        func()
        print("粉刷")
        print("装门")
    print("装饰完成")

    return wrapper

# @decorator ##运行了decorator函数
def house():
    print("毛坯房")


# @decorator
def house2():
    print("简装")
"""
@decorator 的运作：
1、house2 为被装饰函数
2、将 被装饰函数 作为参数 传给装饰器 
3、执行了 装饰器 函数
4、将返回值 wrapper 又赋值给 house2
"""
# house2()



######### 多层装饰器
def decorator1(func):
    print("装饰一开始")
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print("粉刷")
    print("装饰一结束")

    return wrapper

def decorator2(func):
    print('装饰器二开始')
    def wrapper(*args,**kwargs):
        print("装门1")
        func(*args,**kwargs)
        print("装门2")
    print("装饰器二结束")

    return wrapper


# @decorator2
# @decorator1 ###多层装饰器，先用离函数近的那个装饰器
def house3():
    print("毛坯房")
# house3()

###### 带参数的装饰器
"""
带参数的装饰器是三层的
最外层的函数负责接受装饰器参数
里面的内容还是装饰器的内容
"""

def outer(a): ## 负责接受装饰器的参数
    def decorator3(func):  ## 负责接受函数 ，接受不了装饰器参数，所以要在外面在加一层。
        def wrapper(*args,**kwargs):
            func(*args,**kwargs)
            nonlocal a
            a += 1
            print("a:",a)
        return wrapper
    return decorator3

@outer(1)
def func2(x):
    print("x:",x)
# func2(3)
