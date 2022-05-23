import numpy as np

############## 方法一 ，用列表推导式 ＋ for

def tuidaoshi(nums):
    result = [i for num in nums for i in num]
    print(result)
    



############## 方法二：用 numpy 库
def np_methon(nums:list):
    arr = np.array(nums)
    res = arr.flatten()
    res.tolist()
    print(res)
    





a = [[1,2],[3,4],[5,6]]
# tuidaoshi(a)
np_methon(a)