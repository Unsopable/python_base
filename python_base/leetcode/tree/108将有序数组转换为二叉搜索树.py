class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        ################## 方法一
        ### 长度为偶数，则肯定是有树差，不为偶数，则可以没有树差        
        ## 递归构建树
        def dg(left,right):
            ### 递归出口
            if left > right:
                return None

            ### 递归体
            ### 取left和right中间左边的元素作为节点
            mid = (right + left) // 2
            root = TreeNode(nums[mid])
            ## 该节点的左节点
            root.left = dg(left,mid-1)
            root.right = dg(mid+1,right)
            return root
        ## 数组长度
        l = len(nums)
        ## 调用递归函数
        root = dg(0,l-1)
        return root


        ############### 方法二：
        # ### 数组的长度
        # l = len(nums)
        # ## 特殊情况，长度为1时直接返回
        # if l == 1:
        #     return TreeNode(nums[0])
        # ##### 长度不为1
        # ### 长度为偶数，则肯定是有树差，不为偶数，则可以没有树差        
        # ## 为偶数时，假设左边树高大于右边树高
        # mid = l // 2
     
        # ## 递归构建树
        # def dg(i,sym):
        #     ## 递归出口
        #     if i < 0 or i >= l:
        #         return None
        #     root = TreeNode(nums[i])
        #     ##递归体
        #     if sym:
        #         root.left = dg(i-1,sym)
        #         root.right = None
        #     else:
        #         root.left = None
        #         root.right = dg(i+1,sym)
        #     return root

        # root = TreeNode(nums[mid])
        # root.left = dg(mid-1,True)
        # root.right = dg(mid+1,False)
        
        # return root
        
    
s = Solution()
# nums = [-10,-3,0,5,9]
nums = [0,1,2,3,4,5]
res = s.sortedArrayToBST(nums)
print(res.val)
