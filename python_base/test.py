# class Point:
#     z = 10
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     ### __delattr__ 魔法 
#     def __delattr__(self,items):
#         print("要删除的是：",items)

# p = Point(14, 5)    
# del p.x
# print(p.x)

# print(Point.mro())
# print(Point.__dict__)


# class A:
#     def foo(self):
#         print("我是A的foo")

# class B(A):
#     pass

# class C():
#     def foo(self):
#         print("我是C的foo")

# class D(B,C):
#     pass

# d = D()
# d.foo()
# print(D.mro())


# def a():
#     b = 1
#     c = 2
#     d = 3
#     print(locals())
# a()    


# print(range(0,11)[2:-2])

#### 不使用中间变量进行交换 ####
#### 方法一：加法方法




from cmath import pi
from ctypes import sizeof
from inspect import isclass, ismethod
from itertools import zip_longest
import json
import math
from mimetypes import init
from operator import le
import os
from platform import python_version_tuple
import random
import sys

import time
from cv2 import sort
from numpy import percentile
import numpy

import pymysql


def add_methon():
    a = 1
    b = 2
    a = a + b
    b = a - b
    a = a - b
    print("交换后的a,b: ",a,b)
# add_methon()

##### 方法二：异或方法
def exc_methon():
    a = 3
    b = 4
    print(bin(a))
    print(bin(b))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("交换后的a,b: ",a,b)
# exc_methon()

def except_exam():
    try:
        1/0
    except ZeroDivisionError:
        print("不能这么做")
    finally:
        print("结束")
# except_exam()

### 一行代码实现 0——100 之间的和
# print(sum(range(0,100)))

# c = [23,42,54]
# d = map(lambda i : i*2 , c)
# print(d) ##<map object at 0x00000244E3CB44E0>
# print(list(d)) ##[46, 84, 108]

# c = [23,42,54]
# d = filter(lambda i: i > 30 , c)
# print(d) ##<filter object at 0x00000219A60444E0>
# print(list(d)) ##[42, 54]

# from functools import reduce
# c = [1,2,3,4]
# d = reduce(lambda x,y : x + y, c)
# print(d)


### 实现类属性私有化
class P():
    def __init__(self) -> None:
        self.__name = "wang"
        self.__age = 23
    
    #### 使用装饰器方法
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age
    

def jinzhi(num):
    print("bin:",bin(num))
    print("oct:",oct(num))
    print("hex:",hex(num))

# jinzhi(10)


# res = json.dumps({"wh":"王鹤鸣"},ensure_ascii=False)
# print(res)


path_ = os.getcwd()
# print(os.listdir(path_))
# print(path_)
for (root,files_dir,file) in os.walk(path_):
    pass
    # print("root:",root)  ###### 该路径下的所有文件夹绝对路径.
    # print("files_dir:",files_dir) #### 该路径下所有文件夹, 包括文件夹里的文件夹
    # print("file:",file) ####该路径下的所有文件，包括文件夹里的文件



# a = random.random()
# print(a)
# b = random.randint(0,10)
# print(b)
# c = random.randrange(0,10) ### 返回随机整数
# print(c)
# d = random.uniform(0,2) ### 随机返回范围的浮点数
# print(d)

# print(os.name)
# print(os.environ)
# print(sys.modules.keys())
# print(sys.argv)


# a = json.dumps({'张素素':18,'王鹤鸣':12},ensure_ascii=False)
# print(a)



# a = {'张素素':18,'王鹤鸣':12}
# print(a.items())
# print(a.keys())
# print(a.items())
# for i in a.values():
#     print(i)
    
# class A:
#     def __init__(self,asd) -> None:
#         self.asd = asd
# b = A(0)

# print(b.a)


# x = 'abc'
# y = ['1','2','3']
# print(x.join(y))  ##1abc2abc3
# print(','.join(x)) ### a,b,c
# print(os.path.join(x,'sda')) ##abc\sda



# a = [1,2,3,4,4,4]
# b = set(a)
# # print(b[0]) ###TypeError: 'set' object does not support indexing
# for i in b:
#     print(i)

# a = [1,2,3,4]
# print(a.index) ###<built-in method index of list object at 0x000001F9BF55DC88>


# a = frozenset([1,2,3,3,3,4,4])
# print(a)  ###frozenset({1, 2, 3, 4})

# b = set([1,2,3,3,3,4,4])
# print(b)  ####{1, 2, 3, 4}

# ######## 改变 普通集合 的值 ##########
# c = b.pop() ### 集合里的pop方法是删除集合的第一个元素 
# print(c) ### 1
# print(b) ### {2, 3, 4}

# ####### 改变 不可变集合 的值 会出现错误########
# d = a.pop() ###AttributeError: 'frozenset' object has no attribute 'pop'

# p = [1,2,3]
# print(p)
# print(p.index(2))
# p.insert(0,4)
# print(p)

# a = [22,12,4,4,22,4,4,4,32,12,1,6,3]
# b = {}
# res = b.fromkeys(a)
# print(res)
# print(list(res))

# print(sorted(set(a),key= a.index))

# dic = {'a':12,'b':21,'c':232}
# dic.pop('a')
# del dic['b']
# print(dic)
# s = "4193 with words"
# l = len(s)
# s = s.strip()
# print(s)
# print(s.isdigit())

# for i,v in enumerate(s[1:]):
#     print(i,v,type(v))
# print(int("-0012"))
# print(math.ceil(3.5))



# print("a" and "b")  ### b
# print('' or "c")  ### c
# print('' or 0)  ####0

 

# import sys

# for line in sys.stdin:
#     a = line.split()
#     print(nt(a[0]) + int(a[1]))

# a = [1,2,34,5]
# b = [123]
# c = sorted(a + b)
# a.insert(1,4)
# print(c)


# dic = {'a':'1','b':'2'}
# dic = {'c':'1','d':'2'}
# def func(a,b):
#     print(a,type(a))
#     print(b,type(b))
# func(**dic)


# a = {"a":2,"b":3,"c":4}
# # b = a.pop() ##TypeError: pop expected at least 1 arguments, got 0
# b = a.pop('a')
# print(a,b) ##{'b': 3, 'c': 4}   2

# res = os.path.splitext('test.txt')
# print(res)
# a = dict()
# a['1'] = 1
# a['2'] =2
# a.update({3:3})
# print(a.get(3,1))

# b = [1,2]
# print(b[:0])

# prerequisites = [[1,4],[2,4],[3,1],[3,2]]

# dic = dict()
# dic.items()
# for prerequisite in prerequisites:
#     # print(type(prerequisite))
#     for index,content in enumerate(prerequisite):
#         # print(index,content)
#         dic[content] = list(set(dic.get(content,[]) + prerequisite[:index]))
# print(dic)
# numCourses = 5   
# for key,val in dic.items():
#     ### 如果字典的值为空，则表示这门课能学习
#     if not val:
#         numCourses -= 1
#         ### 把这门课从字典中去除

#         print(dic)
#         ### 其他课，如果有val为前置课，就可以pop掉
#         # dic = { i:v.pop(key) for i,v in dic.items()}
#         for i,v in dic.items():
#             if key in v:
#                 v.remove(key)
#                 dic[i] = v
#     else:
#         continue
#     print(dic)   
# print(numCourses-1)

    
    
# numCourses = 4
# for key,val in dic.items():
#     ### 如果字典的值为空，则表示这门课能学习
#     if not val:
#         numCourses -= 1
#         ### 其他课，如果有val为前置课，就可以pop掉
#         dic = { i:v.pop(key) for i,v in dic.items()}
#     else:
#         continue
# print(numCourses)

# coming = { i:len(v) for i,v in dic.items()}
# print(dic)
# print(coming)



# a = [2,'23',[2,3,4]]
# c = a[:]
# b = [2,'23',[2,3,4]]



# print(a == b)
# print(a is b)

# print(id(a[2]))
# print(id(b[2]))
# print(id(c[2]))

# a[2].append(23)
# print(c[2])

# a = [1,2,3,4]
# b = [1,2,3,4]
# c = zip(*(a,b))
# for i in c:
#     print(type(i))
# print(c)

# class A():
#     def __init__(self,c) -> None:
#         self.c = c
#     def meth(self):
#         print('asd')
        
# # print(A.meth)
# a = A(323)
# print(a.__dict__)


# def monkey_patch():
#     print("monkey_patch")

# a.meth = monkey_patch
# a.meth() ### 打印的是 monkey_patch，这就是所谓的猴子补丁
# print(dir(A))
# print(getattr(a,'c'))

# import numpy as np
# print(np.__file__)
# print(isclass(A))
# print(ismethod(a.meth))



# class A(object):
#     def go(self):
#         print( "go A go!")
#     def stop(self):
#         print ("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")

# class B(A):
#     def go(self):
#         super(B, self).go() 
#         print ("go B go!")
        
# class C(A):
#     def go(self):
#         super(C, self).go()
#         super().go()
#         print( "go C go!")
#     def stop(self):
#         super(C, self).stop()
#         print ("stop C stop!")
# class D(B,C):
#     def go(self):
#         super(D, self).go()
#         print ("go D go!")
#     def stop(self):
#         super(D, self).stop()
#         print ("stop D stop!")
#     def pause(self):
#         print ("wait D wait!")
# class E(B,C):
#     pass

# a = A()
# b = B()
# c = C()
# d = D()
# e = E()

# a.go()
# b.go()
# c.go()
# d.go()
# e.go()
# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()


# a = [[12],32,34]
# b = a.copy()
# print(b)
# print(id(a),id(b))
# print(id(a[0]),id(b[0]))
# print(id(a[1]),id(b[1]))
# a.append(3)
# print(id(a),id(b))

# print(dir(a))
# print(help(a))

# a = [1,2,3,4]
# a = list(map(lambda x : x**2, a ))
# print(a)



# a = [1,2,3,4,5]
# res1 = list(map(lambda x: x**2,a))
# print(res1)

# res2 = [x for x in res1 if x>10]
# print(res2)

# a = random.randint(0,4)
# print(a)
# b = random.randrange(0,10,2)
# print(b)
# c = random.random()
# print(c)
# d = [1,2,3,4,5]
# random.shuffle(d)
# print(d)

# s = "ajldjlajfdljfddd"
# ####字典方法去重
# d = dict()
# for n in s:
#     d[n] = 1
# res = list(d.keys())
# print(res)

# res = sorted(res,reverse=False)
# res = ''.join(res)
# print(res)


# s = [1,2,3,4,5,6,7,8,9]
# ### 用filter方法求出列表所有级数并构造新列表
# res = list(filter(lambda x:x % 2 != 0,s))
# print(res)

# import datetime
# print(datetime.datetime.now())
# print("当天是星期 ", datetime.datetime.now().isoweekday()) ##当天是星期  3
# print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')) ##2022/05/04 11:22:48


# a = [1,2,3]
# b = [4,5,6,7]
# res = [i for i in zip(a,b)]
# print(res)

# a = [[1,2],[3,4]]
# print([i for i in zip(*a)])

# a = [1,2,3,4,5]
# print(all(a)) ## True
# b = [0,1,2,3,4] 
# print(all(b)) ## False
# print(any(b)) ## True 

# s = "Hello world ha ha"
# res1 = s.replace(" ","")
# print(res1) ## Helloworldhaha
# res2 = s.replace(" ","/")
# print(res2) ## Hello/world/ha/ha

# l = s.split(" ")
# print(l)
# res3 = "".join(l)
# print(res3)

# a = (i for i in range(3))
# print(a)
# print(type(a))

# def generator():
#     yield from [1,2,3,4]
# a = generator()
# print(type(a))  ###<class 'generator'>
# print(next(a)) ## 1
# print(a.__next__()) ## 2

# class Person():
#     def __del__(self):
#         print("销毁对象")
#     @property
#     @set
# p = Person()
# del p


# s.isdigit()

# try:
#     s = int(s)
# except:
#     print("NO")

# s = s.strip()
# res = ''.join(s)

# f1 = float(s)

# i = int(s)

# f2 = float(i)

# if f1 == f2:
#     print("no")



# def func(a_days,b_days,c_days):
#     ## 用列表存放天数
#     days = [0] * 7
#     days[0] = 1
#     for i,v in enumerate(days):
#         if (i == 0 or i == 4 or i == 5) and a_days>0:
#             a_days -= 1
#             ### 判断day[i]前面是否加1了，前面加1，后面才能加1
#             if((days[i - 1] - days[i]) == -1):
#                 days[i] += 1
#             else:
#                 break
#         if (i == 1 or i == 7) and b_days > 0:
#             b_days -= 1
#                 ### 判断day[i]前面是否加1了，前面加1，后面才能加1
#             if((days[i - 1] - days[i]) == 1):
#                 days[i] += 1
#             else:
#                     break
#         if (i == 2 or i == 3) and c_days > 0:
#             c_days -= 1
#             ### 判断day[i]前面是否加1了，前面加1，后面才能加1
#             if((days[i - 1] - days[i]) == 1):
#                 days[i] += 1
#             else:
#                 break
#     return days

# a = int(ipt[0])
# b = int(ipt[2])
# c = int(ipt[4])
# ##print(a,b,c)
# a_days = a // 8
# b_days = b // 5
# c_days = c // 7
# def func(a_days,b_days,c_days):
#     ## 用列表存放天数
#     days = [0] * 7
#     for i,v in enumerate(days):
#         if (i == 0):
#             if (days[0] == days[6]):
#                 days[0] += 1
#             else:
#                 break
#         if (i == 4 or i == 5) and a_days>0:
#             a_days -= 1
#             ### 判断day[i]前面是否加1了，前面加1，后面才能加1
#             if((days[i] - days[i-1]) == -1):
#                 days[i] += 1
#             else:
#                 break
#         if (i == 1 or i == 7) and b_days > 0:
#             b_days -= 1
#                 ### 判断day[i]前面是否加1了，前面加1，后面才能加1
#             if((days[i] - days[i-1]) == -1):
#                 days[i] += 1
#             else:
#                 break
#         if (i == 2 or i == 3) and c_days > 0:
#             c_days -= 1
#             ### 判断day[i]前面是否加1了，前面加1，后面才能加1
#             if((days[i] - days[i-1]) == -1):
#                 days[i] += 1
#             else:
#                 break
#     return days

# if a_days == 0:
#     print(0)
# else:
#     days = func(a_days,b_days,c_days)
#     print(days)
#     max_time = max(days)
#     days.reverse()
#     i = days.index(max_time)
#     result = ((max_time-1)*7 + (7-i))
#     ##print(result)

def climbStairs(n):
    if n == 0 or n == 1 or n==2:
        return 1
    return climbStairs(n - 1) + climbStairs(n - 2) + climbStairs(n-3)


res = climbStairs(3)
print(res)
