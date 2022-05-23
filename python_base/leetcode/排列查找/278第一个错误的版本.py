# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
def isBadVersion(res):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ##### 二分查找
        ### 先找中间，如果中间是false则向后，如果为True则向前
        ### 递归
        def dg(left,right):
            ## 递归出口
            if left >= right:
                return left
            ## 递归体
            mid = (left + right) // 2
            ## 如果isBaVersion为false，取mid后面的那部分
            if not isBadVersion(mid):
                res = dg(mid+1,right)
             ## 如果isBaVersion为True，取mid前面的那部分
            if isBadVersion(mid):
                res = dg(left,mid-1)
            return res
        ## 使用递归
     
        res = dg(1,n)
        ### 如果是 false True 时，res是取左边的，所以取了false，所以最后要判断一下
        if not isBadVersion(res):
            return res+1
        else:
            return res