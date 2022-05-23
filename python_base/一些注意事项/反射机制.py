###### getattr,setattr,hasattr,delattr 四种反射机制

class A():
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    
    ### 定义方法
    def run(self):
        print("A在跑")
        
        
        
sd = A('a的数值','b的数值')
##### getattr方法【用 字符串 方法 获取对象的属性 和 方法】
print(getattr(sd,'a')) ##### a的数值
print(getattr(sd,'run')) ### 获取了run方法的地址<bound method A.run of <__main__.A object at 0x000001D0CC578D30>> 
func = getattr(sd,'run')
func()  ###A在跑

##### setattr方法 【修改对象属性，用字符串的方法】
setattr(sd,'a','1')
print(sd.a) ##### 1


##### hasattr 方法 【是否 有该对象的属性   字符串方式】
print(hasattr(sd,'a')) #### True

##### delattr 方法 【删除对象属性  字符串方式】
delattr(sd,'a')
# print(sd.a) ####### AttributeError: 'A' object has no attribute 'a'
