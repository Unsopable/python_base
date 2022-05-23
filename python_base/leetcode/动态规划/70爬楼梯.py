"""假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？"""


import locale
from unittest import result


class Solution:
    def climbStairs(self, n: int) -> int:
        ### 可以联想到 二叉树 解决
        results = 0
        def select(n):
            ## 如果 n 小于0 时，退出递归
            if n < 0:
                return
            ####如果 n 等于 0 时，在计数器上加一，在退出
            if n == 0:
                nonlocal results
                results += 1
                return
            ### 左边 树枝
            select(n-1)
            ### 右边 树枝
            select(n-2)
            
        select(n)
        return results

obj = Solution()
res = obj.climbStairs(38)
print(res)
