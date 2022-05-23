def minPathSum(grid):
    ####### 动态规划，走每一步与前面的一步都有关
    m = len(grid)
    n = len(grid[0])
    #### 循环遍历grid,直接再grid修改每个节点的最小总和，一直到最右下角
    for i in range(m):
        for j in range(n):
            ### i 和 j 都为0,则不改变grid对应位置的值
            if i == 0 and j == 0:
                continue
            ## 如果i为0，则该节点只能从左边节点过来
            elif i == 0 :
                grid[i][j] += grid[i][j-1]
            ## 如果j为0,则表示该节点只能从上节点过来
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            ## 其他的节点都可以从上和左边来，比较两边来的大小
            else:
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
                
    return grid[-1][-1]
grid = [[1,3,1],[1,5,1],[4,2,1]]
res = minPathSum(grid)
print(res)


#### 滚动数组
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# dp = [float('inf')] * (len(grid[0])+1)
# dp[1] = 0
# for row in grid:
#     for idx, num in enumerate(row):
#         dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
# print(dp[-1])