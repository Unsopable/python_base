## 递归函数就是：函数自己调用自己
##特点：1.递归函数必须要设有终点（出口）；2.通常会有一个入口


def sum(n): ##入口为n
    ##设置终点
    if n == 0:
        return n
    else:
        return n + sum(n - 1)

s = sum(10)
print(s)
