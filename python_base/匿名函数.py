import functools

### 找出最大的‘a’值，字典
list1 = [{'a': '10', 'b': '20'}, {'a': '15', 'b': '20'}, {'a': '12', 'b': '20'}]
res = max(list1, key=lambda x: x['a'])
# print(res)

### map函数
list2 = [1, 2, 3, 4, 5]
res1 = map(lambda x: x + 2, list2)
# print(list(res1))

###reduce,对列表中的元素，进行加减乘除运算,需要有两个参数
res2 = functools.reduce(lambda x, y: x * y, list2)
# print(res2)
### pop
# print(list2.pop(2))
# print(list2)

####拆包，装包
tuple1 = (1,)
x, *y = tuple1
# print(x)
# print("y:",y)
# print("*y:",*y)### *y里面啥也没有
tuple2 = (1, 2, 3, 4)
x1, *y1 = tuple2
# print(x1)
# print("y1:", y1)##[2, 3, 4],装包
# print("*y1:", *y1)##2, 3, 4
#
# print(*[5,6,7,8])#拆包

####可变参数,可变关键字参数
def add(a,*args,**kwargs):
    print("a:",a)
    print("args:",args)
    print("kwargs:",kwargs)
add(1,2,3,k=1)





