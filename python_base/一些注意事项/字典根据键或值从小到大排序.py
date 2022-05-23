
########## 根据键，进行排序 ###########
def by_key(dic:dict):
    ### 先把 dic 变为 列表
    mid = dic.items()
    print(list(mid))
    ### 然后 排序，在将排序后的列表变为字典
    mid = sorted(mid,key=lambda i:i[0])
    print(mid)
    res = dict(mid)
    print(res) 

def by_key2(dic:dict):
    #### 一步解决
    res = dict(sorted(dic.items(),key=lambda i:i[0]))
    print(res)



########## 根据值，进行排序 ###########
def by_value(dic:dict):
        #### 一步解决 将 i[0] 改为 i[1]
    res = dict(sorted(dic.items(),key=lambda i:i[1]))
    print(res)


dic={"name":1223123,"age":18,"city":2345,"tel":1362626627}
# by_key(dic)
# by_key2(dic)
by_value(dic)