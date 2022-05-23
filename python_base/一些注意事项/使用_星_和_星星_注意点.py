##### 使用 ** 时，字典里的 键 必须和函数里的形参名字相同

# dic = {'c':'1','d':'2'} ##TypeError: func() got an unexpected keyword argument 'c'
dic = {'a':'1','b':'2'}
def func1(a,b):
    print(a,type(a))
    print(b,type(b))
    
# func1(**dic)


s = (1,2,3)
def func2(a,b,c):
    print(a,b,c)
     
# func2(*s) ### 1 2 3

