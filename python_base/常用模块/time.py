import time

t1 = time.time()###获取时间戳
# print(t1)

t2 = time.strftime("%Y-%m-%d %H:%M:%S")
# print(t2)

t3 = time.localtime(t1)##将时间戳转换为struct_time对象
print(t3)
# print(t3.tm_year)

t4 = time.mktime(t3)###将struct_time对象转换为时间戳
print(t4)