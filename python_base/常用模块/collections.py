from collections import namedtuple,Counter

##### 命名元组
person = namedtuple('person',['age','sex'])
zhangsusu = person(17,'女')
print(zhangsusu.age,'  ',zhangsusu.sex)

####### 计数器
s = "asdsfsasdasffad"
print(Counter(s))