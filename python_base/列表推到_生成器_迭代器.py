######### 列表推导 #######
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [i for i in list1 if i % 2 == 0]
# print(list2)

# list1是偶数，返回偶数，是奇数，加1
##含else时，if写在for前面
list3 = [i if i % 2 == 0 else i + 1 for i in list1]
# print(list3)

##########生成器 ########
##写法一：将列表推导的[]改为()
g = (i for i in list1 if i % 2 == 0)
# print(g)##<generator object <genexpr> at 0x0000025B302F5CA8>
# print(g.__next__())#2
# print(g.__next__())#4
v = next(g)
# print(v)#6

##写法二：使用yield关键字
def genera():
    n = 0
    while True:
        n += 1
        yield n
g1 = genera()
# print(g1)##<generator object genera at 0x0000026C15A05D58>
# print(next(g1))#1
# print(g1.__next__())#2

##send方法
def gen2():
    i = 0
    while i<5:
        temp = yield i
        print("temp:",temp)
        i += 1
    return '没有更多数据'

# g2 = gen2()

#### 首先要 send 一个 None值 （必须）
# print(g2.send(None)) # 0

# v2 = g2.send("3")#temp: 3
# print(v2)#1
# v3 = g2.send("6")#temp: 6
# print(v3)#2
# g2.__next__()
# g2.__next__()
# g2.__next__()##error:StopIteration: 没有更多数据

#######迭代器#######
"""
可迭代对象：1、生成器；2、元组，列表，集合，字典，字符串
可迭代对象（除生成器）要变成迭代器，要用iter()函数
生成器就是迭代器的一种
"""
lis4 = [1,2,3,4,5,6]
# next(lis4) ##TypeError: 'list' object is not an iterator
###将列表lis4变为迭代器
lis4 = iter(lis4)
# print(next(lis4))##1
