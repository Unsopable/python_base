def func(nums):
    res = [[num for num in range(1,nums)] [i:i+3] for i in range(0,nums - 1,3)]
    print(res)

func(100)


