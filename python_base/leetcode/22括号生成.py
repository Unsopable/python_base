##数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合

## 先把每种可能都列举出来，然后在剪枝（二叉树形式，递归写）
## 保存结果
res = []
n = 3


def all_maybe(con, left, right):
    ## 找到所有组合后，要剪切树枝 (left,right表示有几个左右括号)
    if left > n or right > n or right > left:
        return

    ## 递归的出口 con表示一条支线的内容,n为几对括号
    ## 如果括号个数大于 2n 则找打出口
    ####### 找到了所有的组合
    if len(con) == 2 * n:
        res.append(con)
        return

    ## 加左括号
    all_maybe(con + '(', left + 1, right)
    ## 加右括号
    all_maybe(con + ')', left, right + 1)

all_maybe("", 0, 0)
print(res)
