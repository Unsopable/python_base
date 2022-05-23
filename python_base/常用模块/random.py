import random


n1 = random.random() ### 0 到 1 之间的随机小数
# print(n1)

n2 = random.randint(1,10) ### 1 到 10 之间的随机整数
# print(n2)

l3 = [1,2,3,4,5]
c1 = random.choice(l3) ##随机选择列表内容
# print(c1)

random.shuffle(l3) ##随机打乱列表顺序
# print(l3)