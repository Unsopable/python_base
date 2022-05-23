a = [1,3,4,5,6]
b = [5,6,7,8,9]

######### 交集
# jiaoji1 = [i for i in b if i in a]
# ### 将列表变为集合，使用集合中的方法
# jiaoji2 = list(set(a).intersection(set(b)))
# ## 集合还可用 逻辑运算符
# jiaoji3 = list(set(a) & set(b))
# print(jiaoji1)
# print(jiaoji2)
# print(jiaoji3)

# ######### 并集
# bingji1 = list(set(a).union(set(b)))
# bingji2 = list(set(a) | set(b))
# print(bingji1)
# print(bingji2)

# ######### 差集
### a中有，b中没有
chaji1 = list(set(a).difference(set(b)))
### b中有，a中没有
chaji2 = list(set(b).difference(set(a)))
print(chaji1)
print(chaji2)

####### 交叉补集
jiaocha1 = list(set(a).symmetric_difference(set(b)))
jiaocha2 = list(set(a) ^ set(b))
print(jiaocha1) ##[1, 3, 4, 7, 8, 9]
print(jiaocha2) ### [1, 3, 4, 7, 8, 9]


