##### 回调函数的定义和用法
def myFunc(st):
    print("myFunc被调用%s"%st)

def reCall(arg,func):
    func(arg)

reCall("结束",myFunc)