###########  列表遍历时删除元素的正确做法 ###########

##### 方法一：遍历在新在列表操作，删除时在原来的列表操作
import re


def delet01(l):
    ## 复制一个列表
    copy_l = l[:]
    ### 在复制的列表里遍历，在原来的列表里进行删除
    for num in copy_l:
        ## 如果 num 大于5，则删除
        if num > 5:
            l.remove(num)
            
    print(l)


##### 方法二：使用过滤器：filter()方法：
def filter_methon(l):
    result = filter(lambda x:x>5,l)
    print(result)  ### filter() 返回的是 可迭代对象
    print(list(result))


##### 方法三：使用倒序遍历方法：
def reverse_methon(l):
    length = len(l)
    for i in range(len(l) - 1,-1,-1):
        if l[i] > 5:
            l.pop(i)

    print(l)



##### 方法四：列表生成器方法
def create_methon(l):
    result = [num for num in l if num < 5]
    print(result)

a = [1,10,3,8,5,6,55,2,76]


# delet01(a)
# filter_methon(a)
reverse_methon(a)
# create_methon(a)


