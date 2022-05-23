a = [22,12,4,4,22,4,4,4,32,12,1,6,3]

###### 方法一：用字典
b = {}
res = b.fromkeys(a)
print(res)  ####{22: None, 12: None, 4: None, 32: None, 1: None, 6: None, 3: None}
print(list(res)) ### [22, 12, 4, 32, 1, 6, 3]



###### 方法二：用sorted 和 set
print(sorted(set(a),key= a.index)) #####[22, 12, 4, 32, 1, 6, 3]

##### 方法三：用遍历
res = []
for i in a:
    if i not in res:
        res.append(i)
print(res) ####### [22, 12, 4, 32, 1, 6, 3]