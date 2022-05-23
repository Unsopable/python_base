try:
    for n in range(5):
        if (n > 3):
            raise Exception("数字 {} 大于3,异常".format(n))
        print(n)
### as 表示给 Exception 命名
except Exception as ex:
    print(ex)
finally:
    print("不管如何,finall都会执行")