############ 快速排序方法 #############

"""def quick_sort(nums, begin, end):
    ### 基准数，去列表首位
    tmp = nums[begin]
    fin_begin = begin
    begin += 1
    ## 递归出口
    if (begin >= end):
        return
    ##递归里面的方法   ***** 注意：左边先动，直到找到比基准数小的数
    while (begin != end):
        ## 如果比基准数大则 左边减一，继续循环
        if (nums[end] >= tmp):
            end -= 1
            continue
        ## 直到找到比 基准数小的时候
        else:
            ## 开始动右边
            while (begin != end):
                if (nums[begin] < tmp):
                        begin += 1
                        continue
                else:
                        ## 如果大则发生change
                        change = nums[begin]
                        nums[begin] = nums[end]
                        nums[end] = change

    ## 找到基准数该放的位置
    nums[fin_begin] = nums[end]
    nums[end] = tmp
    ## 开始递归
    quick_sort(nums,0,begin-1)
    quick_sort(nums,begin+1,len(nums)-1)"""


############ 快速排序方法 #############
def quick_sort(nums, begin, end):
    ## 递归退出
    if (begin > end):
        return
    ## 使用 i,j 表示每段列表的左和右，不改边传入的 begin 和 end 【非常中要】
    i = begin
    j = end
    ## 选取每段列表的第一个数为基准数
    tmp = nums[begin]
    ## 递归里面的方法    ***** 注意：右边先动，直到找到比基准数小的数
    while (i != j):
        ## 如果右边的数大于等于基准数，且右边位置大于左边位置。则 右边向左边移一位
        ## ******** 注意用 while ，不要用 if
        while (nums[j] >= tmp and i < j):
            j -= 1
        ## 如果左边的数小于等于基准数，且右边位置大于左边位置。则 左边向右边移一位
        while (nums[i] <= tmp and i < j):
            i += 1

        #### 交换 左右的 数
        if (i < j):
            change = nums[i]
            nums[i] = nums[j]
            nums[j] = change

    ## 找到了 基准数的位置
    nums[begin] = nums[i]
    nums[i] = tmp

    ## 开始递归【先从左段开始，然后右段】
    quick_sort(nums, begin, i - 1)
    quick_sort(nums, i + 1, end)


############ 冒泡排序方法 #############
def bubble(nums):
    ## 前一个数和后一个数作比较
    length = len(nums)
    ## 第一个循环是 数字要排几次 （如果是3个数，则只要排2次。因为两次排完后最后一个数不用排了）
    for i in range(0,length-1):
        ## 第二个循环是 要比较几次
        for j in range(length - i - 1):
            ## 比较大小
            if (nums[j] > nums[j+1]):
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp

if __name__ == '__main__':
    ## 需要排序的数组
    nums = [12775,18021,5194,11046,7074,5408,13928,-4107,19755,3899,17786]
    ## 使用快速排序
    quick_sort(nums, 0, len(nums) - 1)
    ### 使用冒泡排序

    # bubble(nums)
    print(nums)

