
nums = [-2,1,-3,4,-1,2,1,-5,4]


def find_max(nums):
    # ## 如果nums只有一个数，则直接返回该数
    # if len(nums) == 1:
    #     return nums[0]
    # res = []
    tmp = nums[0]
    max_ = tmp
    n = len(nums)
    for i in range(1, n):
        # tmp加上下一个值，大于下一个值，则继续
        if tmp + nums[i] > nums[i]:
            max_ = max(max_, tmp + nums[i])
            tmp = tmp + nums[i]
        else:
            # 否则，连续加值就断了，重新从该节点开始加
            max_ = max(max_, tmp, tmp + nums[i], nums[i])
            tmp = nums[i]
    return max_
