def rob(nums):
     ########## 动态规划：可以分解为 最后一个屋子盗取不，然后找出状态转移方程，最后解决问题
    # n = len(nums)
    # ### 动态规划的储存
    # dp = [0]*(n+1)
    # dp[1] = nums[0]
    # for i in range(2,n+1):
    #     ### 状态转移方程
    #     dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
    # return dp[n]

    ########## 动态规划，优化空间复杂度
    n = len(nums)

    if not nums:
        return 0

    if n == 1:
        return nums[0]

    ### 只需要保留，此时房间的前一个和前两个位置房间的金额
    second, first = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        second, first = first, max(second + nums[i], first)
    
    return first

nums = [1,2,3,1]
print(rob(nums))