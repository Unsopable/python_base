# def a(nums):
#     n = len(nums)
#     if n < 3:
#         return []
#     res = []
#     ######## 暴力破解
#     ##写三个指针
#     for s in range(n):
#         for m in range(s + 1, n):
#             for e in range(m + 1, n):
#                 if nums[s] + nums[m] + nums[e] == 0:
#                     res.append(sorted([nums[s], nums[m], nums[e]]))
#     ### 在结果列表中排除 相同 的列表
#     ## 两个指针
#     delet = set()
#     for l in range(len(res)):
#         for r in range(l+1,len(res)):
#             if res[l] == res[r]:
#                 delet.add(r)
#
#     for i in sorted(delet,reverse=True):
#         del res[i]
#
#     return res
#
#
# res = a([-1,0,1,2,-1,-4])
# print(res)



def three_sum(nums):
    ### 保存结果
    res = []
    length = len(nums)
    if(not nums or length<3):
            return []
    
    ##### 先将数组进行排序
    nums.sort()
    ### 循环排列后的数组
    for i in range(length):
        ## 如果最小数都 大于 0，则直接返回 res
        if nums[i] >= 0:
            return res
        ## 如果 当前数nums[i] 和 前面的的数 nums[i-1]相等，则重新回到循环
        ### 目的是去重
        if (i>0 and nums[i] == nums[i-1]):
            continue
        ### 两个左右指针:
        left = i + 1
        right = length - 1
        ## 如果 左指针 小与 右指针，则一直循环
        while (left < right):
            th_sum = nums[i] + nums[left] + nums[right]
            #### 如果 三个数相加等于 0 ，则方到 res
            if (th_sum == 0):
                res.append([nums[i],nums[left],nums[right]])
                ### 去除重复
                while(left<right and nums[right] == nums[right - 1]):
                    right -= 1
                while(left<right and nums[left] == nums[left+1]):
                    left += 1
                ### 两边都要同时移动
                left += 1
                right -= 1
                
            #### 如果 三个数相加大于0，则移动right
            if(th_sum > 0):
                right -= 1
            #### 如果 三个数相加小于0，则移动left
            if(th_sum < 0):
                left += 1
            
    return res

a = three_sum([-1,0,1,2,-1,-4])
print(a)

