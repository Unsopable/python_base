
def permute(nums):
    length = len(nums)
    if length == 1:
        return [nums]
    #### 存放结果
    res = []
    #### 存放该位置元素是否被使用
    symbol = [False] * length
    ######### 递归 ########
    def dg(depth,symbol,path):
        ### 递归出口
        if depth == length:
            ##### 注意这里使用path.copy(),如果直接用path的话，我path改变，res也就改变了。
            res.append(path.copy())
            # res.append(path)
            return
        #### 递归体
        for i in range(length):
            ### 如果该位置元素被使用，则继续从循环头开始
            if (symbol[i]):
                continue
            ### 该位置没有被选过，就放放到path里面
            path.append(nums[i])
            ### 使用过后，就将位置符，置为True
            symbol[i] = True
            dg(depth+1,symbol,path)
            ##### 回溯
            path.pop()
            symbol[i] = False

    dg(0,symbol,path=[])
    return res

result = permute([1,2,3])
print(result)



# ########### 递归第二种写法 #########
# def dg(nums:list,temp:list): ### temp用于保存每条路径上的值
#     res = []
#     ### 递归出口
#     ### 如果 nums 为空，则表示一条枝递归结束,将temp加到res中
#     if not nums:
#         res.append(temp)
#         return

#     ##### 递归体
#     ### 遍历列表值
#     l = len(nums)
#     for i in range(l):
#         ### 其实就是选择一个数，就从列表里去掉这个数，在从列表取，如此循环
#         dg(nums[:i] + nums[i+1:], temp + [nums[i]])

# dg(nums,[])
# return res